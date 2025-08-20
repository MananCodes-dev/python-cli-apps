# Data Analyzer - Day 21 Data Analysis Tool
# Analyze scraped data and generate insights

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os
from collections import Counter
import re

class DataAnalyzer:
    def __init__(self, csv_file='data_tools/scraped_data.csv'):
        self.csv_file = csv_file
        self.df = None
        self.analysis_results = {}
    
    def load_data(self):
        """Load data from CSV file"""
        try:
            if not os.path.exists(self.csv_file):
                print(f"❌ File not found: {self.csv_file}")
                print("💡 Run the scraper first to generate data!")
                return False
            
            self.df = pd.read_csv(self.csv_file)
            print(f"✅ Loaded {len(self.df)} records from {self.csv_file}")
            return True
            
        except Exception as e:
            print(f"❌ Error loading data: {str(e)}")
            return False
    
    def basic_stats(self):
        """Generate basic statistics about the data"""
        if self.df is None:
            print("❌ No data loaded!")
            return
        
        print("\n" + "="*60)
        print("📊 BASIC DATA STATISTICS")
        print("="*60)
        
        # Dataset info
        print(f"📋 Total Records: {len(self.df)}")
        print(f"📅 Columns: {list(self.df.columns)}")
        print(f"💾 Memory Usage: {self.df.memory_usage(deep=True).sum() / 1024:.1f} KB")
        
        # Data types breakdown
        print(f"\n📚 Content Types:")
        type_counts = self.df['type'].value_counts()
        for content_type, count in type_counts.items():
            percentage = (count / len(self.df)) * 100
            print(f"  {content_type.title()}: {count} ({percentage:.1f}%)")
        
        # Title length analysis
        if 'title' in self.df.columns:
            self.df['title_length'] = self.df['title'].str.len()
            avg_length = self.df['title_length'].mean()
            max_length = self.df['title_length'].max()
            min_length = self.df['title_length'].min()
            
            print(f"\n📝 Title Analysis:")
            print(f"  Average Length: {avg_length:.1f} characters")
            print(f"  Longest Title: {max_length} characters")
            print(f"  Shortest Title: {min_length} characters")
        
        # Store results
        self.analysis_results['basic_stats'] = {
            'total_records': len(self.df),
            'content_types': type_counts.to_dict(),
            'avg_title_length': avg_length if 'title' in self.df.columns else 0
        }
    
    def word_frequency_analysis(self):
        """Analyze most common words in titles"""
        if self.df is None or 'title' not in self.df.columns:
            print("❌ No title data available!")
            return
        
        print("\n" + "="*60)
        print("🔤 WORD FREQUENCY ANALYSIS")
        print("="*60)
        
        # Combine all titles
        all_titles = ' '.join(self.df['title'].astype(str))
        
        # Clean and split words
        words = re.findall(r'\b[a-zA-Z]{3,}\b', all_titles.lower())
        
        # Remove common stop words
        stop_words = {'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 
                     'can', 'her', 'was', 'one', 'our', 'had', 'have', 'this',
                     'from', 'they', 'she', 'been', 'next', 'their', 'said'}
        
        filtered_words = [word for word in words if word not in stop_words]
        
        # Count word frequency
        word_freq = Counter(filtered_words)
        top_words = word_freq.most_common(10)
        
        print("🏆 Top 10 Most Common Words:")
        for i, (word, count) in enumerate(top_words, 1):
            percentage = (count / len(filtered_words)) * 100
            print(f"  {i:2d}. {word.title():<15} - {count:3d} times ({percentage:.1f}%)")
        
        # Store results
        self.analysis_results['word_frequency'] = dict(top_words)
    
    def content_type_analysis(self):
        """Analyze different content types"""
        if self.df is None:
            return
        
        print("\n" + "="*60)
        print("📂 CONTENT TYPE ANALYSIS")
        print("="*60)
        
        for content_type in self.df['type'].unique():
            subset = self.df[self.df['type'] == content_type]
            print(f"\n📌 {content_type.upper()} Analysis:")
            print(f"  Count: {len(subset)}")
            
            if 'title' in subset.columns:
                avg_length = subset['title'].str.len().mean()
                print(f"  Avg Title Length: {avg_length:.1f} characters")
                
                # Show sample titles
                print("  Sample Titles:")
                for i, title in enumerate(subset['title'].head(3), 1):
                    short_title = title[:50] + '...' if len(str(title)) > 50 else title
                    print(f"    {i}. {short_title}")
    
    def time_analysis(self):
        """Analyze scraping timestamps"""
        if self.df is None or 'scraped_at' not in self.df.columns:
            return
        
        print("\n" + "="*60)
        print("⏰ TIME ANALYSIS")
        print("="*60)
        
        try:
            # Convert to datetime
            self.df['scraped_datetime'] = pd.to_datetime(self.df['scraped_at'])
            
            # Extract time components
            self.df['scrape_hour'] = self.df['scraped_datetime'].dt.hour
            self.df['scrape_minute'] = self.df['scraped_datetime'].dt.minute
            
            earliest = self.df['scraped_datetime'].min()
            latest = self.df['scraped_datetime'].max()
            duration = latest - earliest
            
            print(f"📅 Scraping Session Info:")
            print(f"  Started: {earliest}")
            print(f"  Finished: {latest}")
            print(f"  Duration: {duration}")
            print(f"  Records per minute: {len(self.df) / max(1, duration.total_seconds() / 60):.1f}")
            
        except Exception as e:
            print(f"⚠️  Time analysis error: {str(e)}")
    
    def generate_simple_visualizations(self):
        """Create simple text-based visualizations"""
        if self.df is None:
            return
        
        print("\n" + "="*60)
        print("📈 SIMPLE VISUALIZATIONS")
        print("="*60)
        
        # Content type bar chart (text-based)
        print("\n📊 Content Types Distribution:")
        type_counts = self.df['type'].value_counts()
        max_count = type_counts.max()
        
        for content_type, count in type_counts.items():
            bar_length = int((count / max_count) * 30)
            bar = "█" * bar_length
            print(f"  {content_type.title():<10} │{bar:<30}│ {count}")
        
        # Title length histogram (text-based)
        if 'title_length' in self.df.columns:
            print("\n📏 Title Length Distribution:")
            length_bins = pd.cut(self.df['title_length'], bins=5)
            length_counts = length_bins.value_counts().sort_index()
            max_bin_count = length_counts.max()
            
            for bin_range, count in length_counts.items():
                bar_length = int((count / max_bin_count) * 20)
                bar = "▓" * bar_length
                print(f"  {str(bin_range):<15} │{bar:<20}│ {count}")
    
    def create_html_report(self, filename='analysis_report.html'):
        """Create an HTML report of the analysis"""
        if not self.analysis_results:
            print("❌ No analysis results to report!")
            return
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Data Analysis Report - Day 21</title>
            <style>
                body {{ 
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                    margin: 0; 
                    padding: 20px; 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                }}
                .container {{ 
                    max-width: 1200px; 
                    margin: 0 auto; 
                    background: white; 
                    border-radius: 15px; 
                    box-shadow: 0 10px 30px rgba(0,0,0,0.2); 
                    overflow: hidden; 
                }}
                .header {{ 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    color: white; 
                    padding: 40px; 
                    text-align: center; 
                }}
                .content {{ padding: 40px; }}
                h1 {{ margin: 0; font-size: 3em; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }}
                h2 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; margin-top: 40px; }}
                h3 {{ color: #34495e; }}
                .subtitle {{ opacity: 0.9; margin-top: 15px; font-size: 1.3em; }}
                .stat-box {{ 
                    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); 
                    padding: 25px; 
                    margin: 20px 0; 
                    border-radius: 15px;
                    border-left: 5px solid #3498db;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                }}
                .highlight {{ 
                    background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%); 
                    color: white; 
                    padding: 8px 16px; 
                    border-radius: 25px; 
                    font-weight: bold;
                    display: inline-block;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                }}
                .metrics {{ 
                    display: grid; 
                    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
                    gap: 25px; 
                    margin: 30px 0; 
                }}
                .metric-card {{ 
                    background: linear-gradient(135deg, #ecf0f1 0%, #bdc3c7 100%); 
                    padding: 30px; 
                    border-radius: 15px; 
                    text-align: center;
                    box-shadow: 0 6px 12px rgba(0,0,0,0.1);
                    transition: transform 0.3s ease;
                }}
                .metric-card:hover {{ transform: translateY(-5px); }}
                .metric-value {{ 
                    font-size: 3em; 
                    font-weight: bold; 
                    color: #2c3e50;
                    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
                }}
                .metric-label {{ 
                    color: #7f8c8d; 
                    margin-top: 10px; 
                    font-size: 1.1em;
                    font-weight: 500;
                }}
                table {{ 
                    width: 100%; 
                    border-collapse: collapse; 
                    margin: 25px 0;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                    border-radius: 10px;
                    overflow: hidden;
                }}
                th, td {{ 
                    padding: 15px; 
                    text-align: left; 
                }}
                th {{ 
                    background: linear-gradient(135deg, #3498db 0%, #2980b9 100%); 
                    color: white; 
                    font-weight: 600;
                    text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
                }}
                td {{ background: #f8f9fa; }}
                tr:nth-child(even) td {{ background: #e9ecef; }}
                .footer {{ 
                    background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); 
                    color: white; 
                    padding: 30px; 
                    text-align: center; 
                }}
                .progress-bar {{
                    width: 100%;
                    background: #ecf0f1;
                    border-radius: 10px;
                    overflow: hidden;
                    margin: 10px 0;
                }}
                .progress-fill {{
                    height: 25px;
                    background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
                    border-radius: 10px;
                    transition: width 0.3s ease;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🔍 Data Analysis Report</h1>
                    <div class="subtitle">Professional Web Scraping & Analysis Pipeline</div>
                    <div class="subtitle">🗓️ Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
                </div>
                
                <div class="content">
                    <div class="highlight">📊 Executive Summary</div>
                    
                    <div class="metrics">
                        <div class="metric-card">
                            <div class="metric-value">{self.analysis_results.get('basic_stats', {}).get('total_records', 0)}</div>
                            <div class="metric-label">📋 Total Records</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-value">{len(self.analysis_results.get('basic_stats', {}).get('content_types', {}))}</div>
                            <div class="metric-label">📚 Content Types</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-value">{self.analysis_results.get('basic_stats', {}).get('avg_title_length', 0):.0f}</div>
                            <div class="metric-label">📏 Avg Title Length</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-value">{len(self.analysis_results.get('word_frequency', {}))}</div>
                            <div class="metric-label">🔤 Top Words</div>
                        </div>
                    </div>
                    
                    <h2>📊 Dataset Overview</h2>
                    <div class="stat-box">
                        <h3>🎯 Key Metrics</h3>
                        <p><strong>📋 Total Records Analyzed:</strong> {self.analysis_results.get('basic_stats', {}).get('total_records', 0)} items</p>
                        <p><strong>📏 Average Title Length:</strong> {self.analysis_results.get('basic_stats', {}).get('avg_title_length', 0):.1f} characters</p>
                        <p><strong>⚡ Processing Status:</strong> <span style="color: #27ae60; font-weight: bold;">✅ Complete</span></p>
                    </div>
                    
                    <h2>📚 Content Type Distribution</h2>
                    <table>
                        <tr><th>📂 Content Type</th><th>📊 Count</th><th>📈 Percentage</th><th>📉 Distribution</th></tr>
        """
        
        # Add content types to HTML with progress bars
        total_records = self.analysis_results.get('basic_stats', {}).get('total_records', 1)
        for content_type, count in self.analysis_results.get('basic_stats', {}).get('content_types', {}).items():
            percentage = (count / total_records) * 100
            html_content += f"""
                        <tr>
                            <td>📌 {content_type.title()}</td>
                            <td><strong>{count}</strong></td>
                            <td>{percentage:.1f}%</td>
                            <td>
                                <div class="progress-bar">
                                    <div class="progress-fill" style="width: {percentage}%;"></div>
                                </div>
                            </td>
                        </tr>
            """
        
        html_content += """
                    </table>
                    
                    <h2>🔤 Word Frequency Analysis</h2>
                    <div class="stat-box">
                        <h3>🏆 Top 10 Most Common Words</h3>
                        <table>
                            <tr><th>🔢 Rank</th><th>📝 Word</th><th>📊 Frequency</th><th>📈 Usage Pattern</th></tr>
        """
        
        # Add word frequency to HTML
        for i, (word, freq) in enumerate(list(self.analysis_results.get('word_frequency', {}).items())[:10], 1):
            usage_pattern = "🔥 High" if freq > 5 else "📊 Medium" if freq > 2 else "📉 Low"
            html_content += f"""
                            <tr>
                                <td><strong>#{i}</strong></td>
                                <td>📝 {word.title()}</td>
                                <td><strong>{freq}</strong></td>
                                <td>{usage_pattern}</td>
                            </tr>
            """
        
        html_content += f"""
                        </table>
                    </div>
                    
                    <h2>🔍 Technical Details</h2>
                    <div class="stat-box">
                        <h3>⚙️ Processing Information</h3>
                        <p><strong>🕷️ Data Source:</strong> Multi-source web scraper</p>
                        <p><strong>📊 Analysis Engine:</strong> Python pandas + statistical analysis</p>
                        <p><strong>📈 Report Format:</strong> Interactive HTML with CSS styling</p>
                        <p><strong>⏱️ Generation Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                        <p><strong>🎯 Analysis Type:</strong> Comprehensive text and content analysis</p>
                    </div>
                    
                    <h2>🎉 Analysis Summary</h2>
                    <div class="stat-box">
                        <h3>✅ Completed Analysis Types</h3>
                        <ul style="font-size: 1.1em; line-height: 1.6;">
                            <li>📊 <strong>Basic Statistics:</strong> Record counts, data types, memory usage</li>
                            <li>🔤 <strong>Word Frequency:</strong> Most common terms and language patterns</li>
                            <li>📂 <strong>Content Classification:</strong> Type-based data distribution</li>
                            <li>📏 <strong>Length Analysis:</strong> Title and content size metrics</li>
                            <li>📈 <strong>Visual Reports:</strong> Interactive charts and progress indicators</li>
                        </ul>
                    </div>
                </div>
                
                <div class="footer">
                    <h3>🚀 Day 21 Achievement: Data Analysis Pipeline</h3>
                    <p>📈 <strong>Pipeline Status:</strong> ✅ Successfully processed {self.analysis_results.get('basic_stats', {}).get('total_records', 0)} records</p>
                    <p>🎯 <strong>Part of:</strong> 100-Day Developer Roadmap | Building Real-World Data Skills</p>
                    <p>🔗 <strong>Next Phase:</strong> API Integration & Database Storage (Day 22)</p>
                    <p>⭐ <strong>Skills Demonstrated:</strong> Web Scraping • Data Analysis • Report Generation • Pipeline Automation</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        try:
            # Create analytics directory
            os.makedirs('analytics', exist_ok=True)
            filepath = os.path.join('analytics', filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f"✅ HTML report saved to {filepath}")
            return True
            
        except Exception as e:
            print(f"❌ Error creating HTML report: {str(e)}")
            return False
    
    def run_full_analysis(self):
        """Run complete data analysis"""
        print("🔍 Starting comprehensive data analysis...")
        
        if not self.load_data():
            return False
        
        # Run all analyses
        self.basic_stats()
        self.word_frequency_analysis()
        self.content_type_analysis()
        self.time_analysis()
        self.generate_simple_visualizations()
        
        # Create HTML report
        self.create_html_report()
        
        print("\n🎉 Analysis complete! Check the HTML report for detailed results.")
        return True

def main():
    """Main function to run the analyzer"""
    analyzer = DataAnalyzer()
    
    print("📊 Welcome to Data Analyzer!")
    print("Choose an option:")
    print("1. Run full analysis (recommended)")
    print("2. Load data and show basic stats")
    print("3. Word frequency analysis only")
    print("4. Create HTML report")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            analyzer.run_full_analysis()
        elif choice == '2':
            if analyzer.load_data():
                analyzer.basic_stats()
        elif choice == '3':
            if analyzer.load_data():
                analyzer.word_frequency_analysis()
        elif choice == '4':
            if analyzer.load_data():
                analyzer.basic_stats()
                analyzer.word_frequency_analysis()
                analyzer.create_html_report()
        elif choice == '5':
            print("Thanks for using Data Analyzer! 📊👋")
            break
        else:
            print("Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    main()
