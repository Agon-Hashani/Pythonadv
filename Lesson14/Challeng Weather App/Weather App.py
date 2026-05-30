"""
Advanced Data Visualization App
Works with any CSV dataset (Tokyo Weather, IQ by Country, etc.)
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataVisualizer:
    """Advanced data visualization for CSV datasets"""

    def __init__(self, csv_file, output_dir='output'):
        """Initialize visualizer"""
        self.csv_file = csv_file
        self.output_dir = output_dir
        self.df = None
        Path(output_dir).mkdir(parents=True, exist_ok=True)

    def load_data(self):
        """Load CSV data"""
        try:
            self.df = pd.read_csv(self.csv_file)
            logger.info(f"Loaded {len(self.df)} rows from {self.csv_file}")
            logger.info(f"Columns: {self.df.columns.tolist()}")
            return self.df
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise

    def filter_data(self, column, threshold, operator='>='):
        """Filter data based on column and threshold"""
        if operator == '>=':
            filtered = self.df[self.df[column] >= threshold]
        elif operator == '>':
            filtered = self.df[self.df[column] > threshold]
        elif operator == '<=':
            filtered = self.df[self.df[column] <= threshold]
        elif operator == '<':
            filtered = self.df[self.df[column] < threshold]
        elif operator == '==':
            filtered = self.df[self.df[column] == threshold]
        else:
            filtered = self.df

        logger.info(f"Filtered to {len(filtered)} rows (where {column} {operator} {threshold})")
        return filtered

    def sort_data(self, column, ascending=False):
        """Sort data by column"""
        sorted_df = self.df.sort_values(by=column, ascending=ascending)
        logger.info(f"Sorted by {column} (ascending={ascending})")
        return sorted_df

    def get_stats(self, column):
        """Get statistics for a column"""
        stats = {
            'count': len(self.df),
            'mean': self.df[column].mean(),
            'median': self.df[column].median(),
            'std': self.df[column].std(),
            'min': self.df[column].min(),
            'max': self.df[column].max(),
            'q25': self.df[column].quantile(0.25),
            'q75': self.df[column].quantile(0.75),
        }
        return stats

    def create_bar_chart(self, x_col, y_col, title, xlabel, ylabel,
                        color='skyblue', save_path=None, figsize=(14, 8)):
        """Create enhanced bar chart"""

        plt.figure(figsize=figsize)
        bars = plt.bar(self.df[x_col], self.df[y_col], color=color, edgecolor='black', alpha=0.8)

        # Customize
        plt.title(title, fontsize=16, fontweight='bold', pad=20)
        plt.xlabel(xlabel, fontsize=14, fontweight='bold')
        plt.ylabel(ylabel, fontsize=14, fontweight='bold')

        plt.xticks(rotation=90, fontsize=10)
        plt.yticks(fontsize=10)

        plt.grid(axis='y', linestyle='--', alpha=0.8)

        # Add value labels
        plt.bar_label(bars, fmt='%.2f', fontsize=9, color='black')

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            logger.info(f"Chart saved to {save_path}")

        return plt

    def create_horizontal_bar(self, x_col, y_col, title, xlabel, ylabel,
                             color='steelblue', save_path=None, figsize=(12, 10)):
        """Create horizontal bar chart"""

        plt.figure(figsize=figsize)
        bars = plt.barh(self.df[x_col], self.df[y_col], color=color, edgecolor='black', alpha=0.8)

        # Customize
        plt.title(title, fontsize=16, fontweight='bold', pad=20)
        plt.xlabel(xlabel, fontsize=14, fontweight='bold')
        plt.ylabel(ylabel, fontsize=14, fontweight='bold')

        plt.yticks(fontsize=10)
        plt.xticks(fontsize=10)

        plt.grid(axis='x', linestyle='--', alpha=0.8)

        # Add value labels
        plt.bar_label(bars, fmt='%.2f', fontsize=9, color='black')

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            logger.info(f"Chart saved to {save_path}")

        return plt

    def create_gradient_bar(self, x_col, y_col, title, xlabel, ylabel,
                           save_path=None, figsize=(14, 8)):
        """Create bar chart with gradient coloring"""

        plt.figure(figsize=figsize)

        # Create gradient colors
        norm = plt.Normalize(vmin=self.df[y_col].min(), vmax=self.df[y_col].max())
        colors = plt.cm.RdYlGn(norm(self.df[y_col]))

        bars = plt.bar(self.df[x_col], self.df[y_col], color=colors, edgecolor='black', alpha=0.8)

        # Customize
        plt.title(title, fontsize=16, fontweight='bold', pad=20)
        plt.xlabel(xlabel, fontsize=14, fontweight='bold')
        plt.ylabel(ylabel, fontsize=14, fontweight='bold')

        plt.xticks(rotation=90, fontsize=10)
        plt.yticks(fontsize=10)

        plt.grid(axis='y', linestyle='--', alpha=0.8)

        # Add colorbar
        sm = plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn, norm=norm)
        sm.set_array([])
        cbar = plt.colorbar(sm, ax=plt.gca())
        cbar.set_label(ylabel, fontsize=12, fontweight='bold')

        # Add value labels
        plt.bar_label(bars, fmt='%.2f', fontsize=9, color='black')

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            logger.info(f"Gradient chart saved to {save_path}")

        return plt

    def create_histogram(self, column, title, xlabel, ylabel,
                        bins=30, save_path=None, figsize=(12, 6)):
        """Create histogram"""

        plt.figure(figsize=figsize)

        n, bins_edges, patches = plt.hist(self.df[column], bins=bins,
                                          color='skyblue', edgecolor='black', alpha=0.7)

        # Add statistics line
        mean_val = self.df[column].mean()
        median_val = self.df[column].median()

        plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.2f}')
        plt.axvline(median_val, color='green', linestyle='--', linewidth=2, label=f'Median: {median_val:.2f}')

        # Customize
        plt.title(title, fontsize=16, fontweight='bold', pad=20)
        plt.xlabel(xlabel, fontsize=14, fontweight='bold')
        plt.ylabel(ylabel, fontsize=14, fontweight='bold')

        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)

        plt.grid(axis='y', linestyle='--', alpha=0.8)
        plt.legend(fontsize=11)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            logger.info(f"Histogram saved to {save_path}")

        return plt

    def create_box_plot(self, columns, title, ylabel,
                       save_path=None, figsize=(12, 6)):
        """Create box plot"""

        plt.figure(figsize=figsize)

        box_data = [self.df[col].dropna() for col in columns]
        bp = plt.boxplot(box_data, labels=columns, patch_artist=True)

        # Color the boxes
        colors = plt.cm.Set3(np.linspace(0, 1, len(columns)))
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)

        # Customize
        plt.title(title, fontsize=16, fontweight='bold', pad=20)
        plt.ylabel(ylabel, fontsize=14, fontweight='bold')

        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)

        plt.grid(axis='y', linestyle='--', alpha=0.8)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            logger.info(f"Box plot saved to {save_path}")

        return plt

    def create_line_plot(self, x_col, y_col, title, xlabel, ylabel,
                        save_path=None, figsize=(14, 6)):
        """Create line plot"""

        plt.figure(figsize=figsize)

        plt.plot(self.df[x_col], self.df[y_col], marker='o', linestyle='-',
                linewidth=2, markersize=6, color='steelblue')

        # Customize
        plt.title(title, fontsize=16, fontweight='bold', pad=20)
        plt.xlabel(xlabel, fontsize=14, fontweight='bold')
        plt.ylabel(ylabel, fontsize=14, fontweight='bold')

        plt.xticks(rotation=45, fontsize=10)
        plt.yticks(fontsize=10)

        plt.grid(True, linestyle='--', alpha=0.8)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            logger.info(f"Line plot saved to {save_path}")

        return plt

    def create_scatter_plot(self, x_col, y_col, title, xlabel, ylabel,
                           save_path=None, figsize=(12, 8)):
        """Create scatter plot"""

        plt.figure(figsize=figsize)

        # Color by y values
        scatter = plt.scatter(self.df[x_col], self.df[y_col],
                            c=self.df[y_col], cmap='viridis',
                            s=100, alpha=0.6, edgecolors='black')

        # Customize
        plt.title(title, fontsize=16, fontweight='bold', pad=20)
        plt.xlabel(xlabel, fontsize=14, fontweight='bold')
        plt.ylabel(ylabel, fontsize=14, fontweight='bold')

        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)

        plt.grid(True, linestyle='--', alpha=0.8)

        # Add colorbar
        cbar = plt.colorbar(scatter)
        cbar.set_label(ylabel, fontsize=12, fontweight='bold')

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            logger.info(f"Scatter plot saved to {save_path}")

        return plt

    def create_pie_chart(self, column, title, save_path=None, figsize=(10, 8)):
        """Create pie chart"""

        plt.figure(figsize=figsize)

        # Get top categories
        top_data = self.df[column].value_counts().head(10)

        colors = plt.cm.Set3(np.linspace(0, 1, len(top_data)))
        wedges, texts, autotexts = plt.pie(top_data.values, labels=top_data.index,
                                            autopct='%1.1f%%', colors=colors, startangle=90)

        # Customize
        plt.title(title, fontsize=16, fontweight='bold', pad=20)

        for text in texts:
            text.set_fontsize(10)
        for autotext in autotexts:
            autotext.set_color('black')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(9)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            logger.info(f"Pie chart saved to {save_path}")

        return plt

    def create_heatmap(self, save_path=None, figsize=(12, 10)):
        """Create correlation heatmap"""

        # Select only numeric columns
        numeric_df = self.df.select_dtypes(include=[np.number])

        if len(numeric_df.columns) < 2:
            logger.warning("Not enough numeric columns for heatmap")
            return None

        plt.figure(figsize=figsize)

        # Calculate correlation
        corr = numeric_df.corr()

        sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0,
                   square=True, linewidths=1, cbar_kws={"shrink": 0.8})

        plt.title('Correlation Heatmap', fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            logger.info(f"Heatmap saved to {save_path}")

        return plt

    def print_summary(self):
        """Print data summary"""
        print("\n" + "=" * 80)
        print("DATA SUMMARY")
        print("=" * 80)
        print(f"Shape: {self.df.shape}")
        print(f"\nFirst rows:\n{self.df.head()}")
        print(f"\nData types:\n{self.df.dtypes}")
        print(f"\nBasic statistics:\n{self.df.describe()}")
        print("=" * 80 + "\n")


# ============================================================================
# TOKYO WEATHER EXAMPLE
# ============================================================================

def tokyo_weather_example():
    """Example: Tokyo weather data analysis"""

    print("\n" + "=" * 80)
    print("TOKYO WEATHER DATA ANALYSIS")
    print("=" * 80 + "\n")

    csv_file = 'data/tokyo_weather.csv'

    try:
        # Create visualizer
        viz = DataVisualizer(csv_file, output_dir='output')
        df = viz.load_data()

        # Print summary
        viz.print_summary()

        # Get temperature column
        temp_col = None
        for col in ['Temperature', 'Temp', 'temperature', 'temp', 'Mean Temperature']:
            if col in df.columns:
                temp_col = col
                break

        if temp_col:
            # Filter data
            filtered_df = viz.filter_data(temp_col, 15, '>=')

            # Sort data
            sorted_df = filtered_df.sort_values(by=temp_col, ascending=False)
            viz.df = sorted_df

            # Get date column
            date_col = None
            for col in ['Date', 'date', 'Day']:
                if col in df.columns:
                    date_col = col
                    break

            if date_col:
                # Create visualizations
                viz.create_line_plot(date_col, temp_col,
                                    'Tokyo Temperature Over Time',
                                    'Date', 'Temperature (°C)',
                                    save_path='output/temperature_trend.png')

                viz.create_histogram(temp_col,
                                   'Temperature Distribution in Tokyo',
                                   'Temperature (°C)', 'Frequency',
                                   save_path='output/temperature_histogram.png')

            print("\nVisualizations created successfully!")

    except FileNotFoundError:
        print(f"Note: {csv_file} not found. Download from Kaggle first.")


