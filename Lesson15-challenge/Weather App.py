"""
Advanced Tokyo Weather Data Analysis App
Combines multiple visualizations: bar charts, line plots, pie charts, and statistical analysis
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class TokyoWeatherAnalyzer:
    """Advanced weather data analyzer with multiple visualization types"""

    def __init__(self, csv_file, output_dir='output'):
        """Initialize the weather analyzer"""
        self.csv_file = csv_file
        self.output_dir = output_dir
        self.df = None
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        logger.info(f"Output directory: {output_dir}")

    def load_data(self):
        """Load and prepare weather data"""
        try:
            self.df = pd.read_csv(self.csv_file)

            # Clean column names
            self.df.columns = self.df.columns.str.strip()

            # Parse date information
            self.df['month'] = self.df['day'].str.split('/').str[0].astype(int)
            self.df['day_of_month'] = self.df['day'].str.split('/').str[1].astype(int)

            # Clean temperature data (handle parentheses for negative values)
            self.df['temperature'] = self.df['temperature'].astype(str)
            self.df['temperature'] = self.df['temperature'].str.replace('(', '-').str.replace(')', '')
            self.df['temperature'] = pd.to_numeric(self.df['temperature'], errors='coerce')

            # Clean other columns
            self.df['humidity'] = pd.to_numeric(self.df['humidity '].str.strip(), errors='coerce')
            self.df['atmospheric pressure'] = pd.to_numeric(self.df['atmospheric pressure'].str.strip(), errors='coerce')

            logger.info(f"✓ Loaded {len(self.df)} rows from {self.csv_file}")
            logger.info(f"✓ Columns: {self.df.columns.tolist()}")
            return self.df

        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise

    def print_summary(self):
        """Print comprehensive data summary"""
        print("\n" + "=" * 80)
        print("TOKYO WEATHER DATA SUMMARY")
        print("=" * 80)
        print(f"Dataset Shape: {self.df.shape}")
        print(f"Date Range: {self.df['year'].min()}/{self.df['month'].min()} to {self.df['year'].max()}/{self.df['month'].max()}")
        print(f"\nFirst 5 rows:\n{self.df.head()}")
        print(f"\nData Types:\n{self.df.dtypes}")
        print(f"\nBasic Statistics:\n{self.df[['temperature', 'humidity', 'atmospheric pressure']].describe()}")
        print("=" * 80 + "\n")

    # ========================================================================
    # 1. TEMPERATURE OVERVIEW
    # ========================================================================

    def temperature_overview(self):
        """Task 1a: Calculate average temperature for entire dataset"""
        avg_temp = self.df['temperature'].mean()
        logger.info(f"✓ Task 1a: Average Temperature = {avg_temp:.2f}°C")
        return avg_temp

    # ========================================================================
    # 2. MONTHLY TEMPERATURES
    # ========================================================================

    def calculate_monthly_temperatures(self):
        """Task 2a: Calculate average temperature for each month"""
        monthly_avg = self.df.groupby('month')['temperature'].mean().reset_index()
        monthly_avg.columns = ['Month', 'Average Temperature']

        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        monthly_avg['Month Name'] = monthly_avg['Month'].apply(lambda x: month_names[x-1])

        logger.info(f"✓ Task 2a: Monthly averages calculated")
        print("\nMonthly Average Temperatures:")
        print(monthly_avg[['Month', 'Month Name', 'Average Temperature']])
        return monthly_avg

    def visualize_monthly_temperatures_bar(self, monthly_avg):
        """Task 2b: Visualize monthly average temperature using bar plot"""
        plt.figure(figsize=(14, 8))

        bars = plt.bar(monthly_avg['Month Name'], monthly_avg['Average Temperature'],
                       color='steelblue', edgecolor='black', alpha=0.8, linewidth=1.5)

        # Customize
        plt.title('Monthly Average Temperature in Tokyo', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Month', fontsize=14, fontweight='bold')
        plt.ylabel('Average Temperature (°C)', fontsize=14, fontweight='bold')

        plt.xticks(fontsize=11)
        plt.yticks(fontsize=11)

        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}°C',
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

        save_path = f'{self.output_dir}/monthly_temperature_bar.png'
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"✓ Task 2b: Monthly bar chart saved to {save_path}")
        plt.show()

    # ========================================================================
    # 3. HIGHS AND LOWS
    # ========================================================================

    def find_highs_and_lows(self):
        """Task 3a: Identify hottest and coldest days with complete row data"""
        hottest_idx = self.df['temperature'].idxmax()
        coldest_idx = self.df['temperature'].idxmin()

        hottest_row = self.df.loc[hottest_idx]
        coldest_row = self.df.loc[coldest_idx]

        print("\n" + "=" * 80)
        print("TEMPERATURE EXTREMES")
        print("=" * 80)
        print(f"\nHOTTEST DAY:")
        print(f"  Date: {hottest_row['year']}/{hottest_row['day']}")
        print(f"  Temperature: {hottest_row['temperature']:.1f}°C")
        print(f"  Humidity: {hottest_row['humidity']:.1f}%")
        print(f"  Atmospheric Pressure: {hottest_row['atmospheric pressure']:.1f} hPa")

        print(f"\nCOLDEST DAY:")
        print(f"  Date: {coldest_row['year']}/{coldest_row['day']}")
        print(f"  Temperature: {coldest_row['temperature']:.1f}°C")
        print(f"  Humidity: {coldest_row['humidity']:.1f}%")
        print(f"  Atmospheric Pressure: {coldest_row['atmospheric pressure']:.1f} hPa")
        print("=" * 80 + "\n")

        logger.info(f"✓ Task 3a: Hottest day = {hottest_row['temperature']:.1f}°C, Coldest day = {coldest_row['temperature']:.1f}°C")
        return hottest_row, coldest_row

    # ========================================================================
    # 4. TEMPERATURE TRENDS
    # ========================================================================

    def visualize_temperature_trends(self):
        """Task 4a: Create line graph showing temperature changes over time"""
        # Create date index
        self.df['date_index'] = range(len(self.df))

        plt.figure(figsize=(16, 7))

        plt.plot(self.df['date_index'], self.df['temperature'],
                marker='o', linestyle='-', linewidth=2, markersize=4,
                color='steelblue', alpha=0.8, label='Daily Temperature')

        # Add trend line
        z = np.polyfit(self.df['date_index'], self.df['temperature'], 3)
        p = np.poly1d(z)
        plt.plot(self.df['date_index'], p(self.df['date_index']),
                "r--", linewidth=2, alpha=0.8, label='Trend Line')

        # Customize
        plt.title('Tokyo Temperature Trends Over Time', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Days (Nov 2022 - Nov 2023)', fontsize=14, fontweight='bold')
        plt.ylabel('Temperature (°C)', fontsize=14, fontweight='bold')

        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)

        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend(fontsize=12, loc='upper left')
        plt.tight_layout()

        save_path = f'{self.output_dir}/temperature_trends.png'
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"✓ Task 4a: Temperature trends line plot saved to {save_path}")
        plt.show()

    # ========================================================================
    # 5. SEASONAL ANALYSIS
    # ========================================================================

    def define_seasons(self, month):
        """Define seasons based on month (Northern Hemisphere)"""
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        else:  # 9, 10, 11
            return 'Fall'

    def calculate_seasonal_temperatures(self):
        """Task 4b: Calculate average temperature for each season"""
        self.df['season'] = self.df['month'].apply(self.define_seasons)

        seasonal_avg = self.df.groupby('season')['temperature'].agg([
            ('Average Temperature', 'mean'),
            ('Min Temperature', 'min'),
            ('Max Temperature', 'max'),
            ('Std Deviation', 'std'),
            ('Count', 'count')
        ]).reset_index()

        # Order seasons chronologically
        season_order = ['Winter', 'Spring', 'Summer', 'Fall']
        seasonal_avg['season'] = pd.Categorical(seasonal_avg['season'], categories=season_order, ordered=True)
        seasonal_avg = seasonal_avg.sort_values('season')

        logger.info(f"✓ Task 4b: Seasonal averages calculated")
        print("\nSeasonal Average Temperatures:")
        print(seasonal_avg)
        return seasonal_avg

    def visualize_seasonal_temperatures_line(self, seasonal_avg):
        """Task 4b: Visualize seasonal average temperature using line plot"""
        plt.figure(figsize=(12, 7))

        plt.plot(seasonal_avg['season'], seasonal_avg['Average Temperature'],
                marker='o', linestyle='-', linewidth=3, markersize=12,
                color='darkgreen', label='Average Temperature', alpha=0.8)

        # Add error bars for range
        plt.fill_between(range(len(seasonal_avg)),
                         seasonal_avg['Min Temperature'],
                         seasonal_avg['Max Temperature'],
                         alpha=0.2, color='green', label='Min-Max Range')

        # Add value labels
        for i, (season, temp) in enumerate(zip(seasonal_avg['season'], seasonal_avg['Average Temperature'])):
            plt.text(i, temp + 1, f'{temp:.1f}°C', ha='center', fontsize=11, fontweight='bold')

        # Customize
        plt.title('Seasonal Average Temperature in Tokyo', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Season', fontsize=14, fontweight='bold')
        plt.ylabel('Temperature (°C)', fontsize=14, fontweight='bold')

        plt.xticks(fontsize=12)
        plt.yticks(fontsize=11)

        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend(fontsize=12, loc='upper left')
        plt.tight_layout()

        save_path = f'{self.output_dir}/seasonal_temperature_line.png'
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"✓ Task 4b: Seasonal line plot saved to {save_path}")
        plt.show()

    # ========================================================================
    # BONUS VISUALIZATIONS
    # ========================================================================

    def create_temperature_distribution_histogram(self):
        """Create histogram of temperature distribution"""
        plt.figure(figsize=(12, 7))

        n, bins, patches = plt.hist(self.df['temperature'], bins=30,
                                    color='skyblue', edgecolor='black', alpha=0.8)

        # Color bars by value
        cm = plt.cm.RdYlGn
        norm = plt.Normalize(vmin=min(patches[0].get_x(), 0), vmax=max(patches[-1].get_x(), 35))
        for patch in patches:
            patch.set_facecolor(cm(norm(patch.get_x() + patch.get_width()/2)))

        # Add mean and median lines
        mean_temp = self.df['temperature'].mean()
        median_temp = self.df['temperature'].median()

        plt.axvline(mean_temp, color='red', linestyle='--', linewidth=2.5, label=f'Mean: {mean_temp:.2f}°C')
        plt.axvline(median_temp, color='green', linestyle='--', linewidth=2.5, label=f'Median: {median_temp:.2f}°C')

        # Customize
        plt.title('Temperature Distribution in Tokyo', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Temperature (°C)', fontsize=14, fontweight='bold')
        plt.ylabel('Frequency', fontsize=14, fontweight='bold')

        plt.xticks(fontsize=11)
        plt.yticks(fontsize=11)

        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend(fontsize=12)
        plt.tight_layout()

        save_path = f'{self.output_dir}/temperature_distribution.png'
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"✓ Temperature distribution histogram saved to {save_path}")
        plt.show()

    def create_seasonal_pie_chart(self, seasonal_avg):
        """Create pie chart for seasonal temperature contribution"""
        plt.figure(figsize=(10, 8))

        colors = ['#87CEEB', '#90EE90', '#FFD700', '#FF8C00']

        wedges, texts, autotexts = plt.pie(seasonal_avg['Average Temperature'],
                                            labels=seasonal_avg['season'],
                                            autopct='%1.1f%%',
                                            colors=colors,
                                            startangle=90,
                                            textprops={'fontsize': 12, 'weight': 'bold'})

        for autotext in autotexts:
            autotext.set_color('black')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(11)

        plt.title('Seasonal Temperature Distribution', fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout()

        save_path = f'{self.output_dir}/seasonal_pie_chart.png'
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"✓ Seasonal pie chart saved to {save_path}")
        plt.show()

    def create_correlation_heatmap(self):
        """Create correlation heatmap for weather variables"""
        plt.figure(figsize=(10, 8))

        # Select numeric columns
        numeric_df = self.df[['temperature', 'humidity', 'atmospheric pressure']].corr()

        sns.heatmap(numeric_df, annot=True, fmt='.3f', cmap='coolwarm', center=0,
                   square=True, linewidths=2, cbar_kws={"shrink": 0.8},
                   vmin=-1, vmax=1)

        plt.title('Weather Variables Correlation Heatmap', fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout()

        save_path = f'{self.output_dir}/correlation_heatmap.png'
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"✓ Correlation heatmap saved to {save_path}")
        plt.show()

    def create_humidity_pressure_scatter(self):
        """Create scatter plot of humidity vs atmospheric pressure"""
        plt.figure(figsize=(12, 8))

        scatter = plt.scatter(self.df['humidity'], self.df['atmospheric pressure'],
                            c=self.df['temperature'], cmap='RdYlGn',
                            s=100, alpha=0.6, edgecolors='black', linewidth=0.5)

        # Customize
        plt.title('Humidity vs Atmospheric Pressure (colored by Temperature)',
                 fontsize=14, fontweight='bold', pad=20)
        plt.xlabel('Humidity (%)', fontsize=12, fontweight='bold')
        plt.ylabel('Atmospheric Pressure (hPa)', fontsize=12, fontweight='bold')

        plt.xticks(fontsize=11)
        plt.yticks(fontsize=11)

        # Add colorbar
        cbar = plt.colorbar(scatter)
        cbar.set_label('Temperature (°C)', fontsize=11, fontweight='bold')

        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()

        save_path = f'{self.output_dir}/humidity_pressure_scatter.png'
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"✓ Humidity vs Pressure scatter plot saved to {save_path}")
        plt.show()

    # ========================================================================
    # MAIN EXECUTION
    # ========================================================================

    def run_complete_analysis(self):
        """Run complete weather analysis with all visualizations"""
        try:
            # Load data
            self.load_data()
            self.print_summary()

            # Task 1: Temperature Overview
            print("\n" + "="*80)
            print("TASK 1: TEMPERATURE OVERVIEW")
            print("="*80)
            avg_temp = self.temperature_overview()
            print(f"Average Temperature for entire dataset: {avg_temp:.2f}°C\n")

            # Task 2: Monthly Temperatures
            print("="*80)
            print("TASK 2: MONTHLY TEMPERATURES")
            print("="*80)
            monthly_avg = self.calculate_monthly_temperatures()
            self.visualize_monthly_temperatures_bar(monthly_avg)

            # Task 3: Highs and Lows
            print("="*80)
            print("TASK 3: HIGHS AND LOWS")
            print("="*80)
            self.find_highs_and_lows()

            # Task 4: Temperature Trends & Seasonal Analysis
            print("="*80)
            print("TASK 4: TEMPERATURE TRENDS")
            print("="*80)
            self.visualize_temperature_trends()

            print("="*80)
            print("TASK 4B: SEASONAL AVERAGE TEMPERATURE")
            print("="*80)
            seasonal_avg = self.calculate_seasonal_temperatures()
            self.visualize_seasonal_temperatures_line(seasonal_avg)

            # Bonus visualizations
            print("\n" + "="*80)
            print("BONUS VISUALIZATIONS")
            print("="*80)
            self.create_temperature_distribution_histogram()
            self.create_seasonal_pie_chart(seasonal_avg)
            self.create_correlation_heatmap()
            self.create_humidity_pressure_scatter()

            print("\n" + "="*80)
            print("✓ ALL ANALYSIS COMPLETE!")
            print("="*80)
            print(f"All visualizations saved to: {self.output_dir}/")

        except Exception as e:
            logger.error(f"Error during analysis: {e}")
            raise


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Initialize analyzer with Tokyo weather data
    csv_file = 'Lesson14/Challeng Weather App/weather_tokyo_data.csv'

    analyzer = TokyoWeatherAnalyzer(csv_file, output_dir='Challeng Weather App/output')
    analyzer.run_complete_analysis()
