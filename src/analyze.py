__author__ = 'Khiem Doan'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from lottery import Lottery
from stations import get_stations_for_date, STATION_CODES
from templates import Render


def colors_from_values(values, palette_name):
    normalized = (values - min(values)) / (max(values) - min(values))
    indices = np.round(normalized * (len(values) - 1)).astype(np.int32)
    palette = sns.color_palette(palette_name, len(values))
    return np.array(palette).take(indices, axis=0)


def generate_station_plots(lottery: Lottery, output_dir: str):
    """Tạo tất cả biểu đồ cho một đài."""
    os.makedirs(output_dir, exist_ok=True)

    results = lottery.get_raw_data()
    sparse_results = lottery.get_sparse_data()

    if results.empty:
        print(f'  No data for {lottery.get_station_name()}')
        return {}

    last_date = results['date'].max()

    # Lấy dữ liệu 1 năm
    start_date = pd.Timestamp(year=last_date.year - 1, month=last_date.month, day=last_date.day)
    small_results = results[(start_date < results['date']) & (results['date'] <= last_date)]
    small_results.reset_index(drop=True, inplace=True)

    if small_results.empty:
        print(f'  Not enough data for {lottery.get_station_name()}')
        return {}

    # Tính loto result cho ngày mới nhất
    numeric_cols = [c for c in small_results.columns if c not in ('date', 'station', 'station_code')]
    recent_results = small_results.iloc[-1][numeric_cols].values
    recent_results = recent_results % 100
    loto_result = []
    for i in range(10):
        category = sorted([d for d in recent_results if d // 10 == i])
        category = [f'{d % 10:1d}' for d in category]
        category = ', '.join(category) if len(category) > 0 else '-'
        loto_result.append(category)

    # Sparse data 1 năm
    last_date_sparse = sparse_results['date'].max()
    start_date_sparse = pd.Timestamp(year=last_date_sparse.year - 1, month=last_date_sparse.month, day=last_date_sparse.day)
    sparse_1_year = sparse_results[(start_date_sparse < sparse_results['date']) & (sparse_results['date'] <= last_date_sparse)]
    sparse_1_year.reset_index(drop=True, inplace=True)
    sparse_1_year = sparse_1_year.drop(columns=['date'])
    counts = sparse_1_year.sum(axis=0)

    max_count = counts.max().round(2)
    min_count = counts.min().round(2)
    mean = counts.mean().round(2)
    std = counts.std().round(2)

    # --- Heatmap ---
    counts_df = counts.reset_index()
    counts_df.columns = ['value', 'freq']
    counts_df = counts_df.astype({'value': int})
    counts_df.sort_values('freq', ascending=False, inplace=True)

    heatmap_data = counts_df.copy()
    heatmap_data['tens'] = heatmap_data['value'] // 10
    heatmap_data['ones'] = heatmap_data['value'] % 10
    heatmap_data = heatmap_data[['tens', 'ones', 'freq']]
    heatmap_data = heatmap_data.pivot(index='tens', columns='ones', values='freq').fillna(0)
    heatmap_data = heatmap_data.astype(int)

    fig, ax = plt.subplots()
    sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='RdYlGn', ax=ax)
    ax.set_title(f'{lottery.get_station_name()} - Detail')
    fig.savefig(f'{output_dir}/heatmap.jpg')
    plt.close(fig)

    # --- Top 10 ---
    bar_data = counts_df[:10].copy()
    bar_data['value'] = bar_data['value'].apply(lambda r: f'{r:02d}')

    fig, ax = plt.subplots()
    palette = reversed(colors_from_values(bar_data['freq'], 'summer'))
    sns.barplot(bar_data, x='value', y='freq', hue='value', palette=palette, ax=ax)
    for bar in ax.containers:
        ax.bar_label(bar, fmt='%d')
    ax.set_title(f'{lottery.get_station_name()} - Top 10')
    fig.savefig(f'{output_dir}/top-10.jpg')
    plt.close(fig)

    # --- Distribution ---
    data = counts_df[['freq']].copy()
    bins = data.max().iloc[0] - data.min().iloc[0] + 1

    fig, ax = plt.subplots()
    sns.histplot(data, kde=True, bins=bins, fill=False, ax=ax)
    kdeline = ax.lines[0]
    xs = kdeline.get_xdata()
    ys = kdeline.get_ydata()
    ax.vlines(mean, 0, np.interp(mean, xs, ys), color='red', linestyles='solid')
    ax.vlines(mean - std, 0, np.interp(mean - std, xs, ys), color='red', linestyles='dashed')
    ax.vlines(mean + std, 0, np.interp(mean + std, xs, ys), color='red', linestyles='dashed')
    ax.vlines(mean - 2 * std, 0, np.interp(mean - 2 * std, xs, ys), color='red', linestyles='dotted')
    ax.vlines(mean + 2 * std, 0, np.interp(mean + 2 * std, xs, ys), color='red', linestyles='dotted')
    ax.set_title(f'{lottery.get_station_name()} - Distribution')
    fig.savefig(f'{output_dir}/distribution.jpg')
    plt.close(fig)

    # Lấy kết quả ngày mới nhất cho template
    last_row = small_results.iloc[-1]
    return {
        'station_name': lottery.get_station_name(),
        'station_code': lottery.get_station_code(),
        'loto_result': loto_result,
        'max_count': max_count,
        'min_count': min_count,
        'mean': mean,
        'std': std,
        'last_date': last_row['date'].strftime('%d-%m-%Y'),
        'special': int(last_row['special']),
        'prize1': int(last_row['prize1']),
        'prize2': int(last_row['prize2']),
        'prize3_1': int(last_row['prize3_1']),
        'prize3_2': int(last_row['prize3_2']),
        'prize4_1': int(last_row['prize4_1']),
        'prize4_2': int(last_row['prize4_2']),
        'prize4_3': int(last_row['prize4_3']),
        'prize4_4': int(last_row['prize4_4']),
        'prize4_5': int(last_row['prize4_5']),
        'prize4_6': int(last_row['prize4_6']),
        'prize4_7': int(last_row['prize4_7']),
        'prize5': int(last_row['prize5']),
        'prize6_1': int(last_row['prize6_1']),
        'prize6_2': int(last_row['prize6_2']),
        'prize6_3': int(last_row['prize6_3']),
        'prize7': int(last_row['prize7']),
        'prize8': int(last_row['prize8']),
    }


if __name__ == '__main__':
    tz = ZoneInfo('Asia/Ho_Chi_Minh')
    now = datetime.now(tz)
    today = now.date()
    if now.time() < datetime.strptime('16:30', '%H:%M').time():
        today -= timedelta(days=1)

    weekday = today.weekday()
    stations = get_stations_for_date(weekday)

    station_results = []
    for station_name in stations:
        station_code = STATION_CODES.get(station_name, station_name.lower().replace(" ", ""))
        print(f'Analyzing: {station_name} ({station_code})')

        lottery = Lottery(station_name)
        lottery.load()

        if lottery.get_raw_data().empty:
            print(f'  No data, skipping')
            continue

        result = generate_station_plots(lottery, f'images/{station_code}')
        if result:
            station_results.append(result)

    # Render README
    if station_results:
        render = Render()
        context = {
            'station_results': station_results,
            'date': today.strftime('%d-%m-%Y'),
        }
        content = render('README.j2', context)
        with open('README.md', 'w', encoding='utf-8') as outfile:
            outfile.write(content)
        print(f'\nREADME.md updated with {len(station_results)} stations')
    else:
        print('\nNo station data to analyze')
