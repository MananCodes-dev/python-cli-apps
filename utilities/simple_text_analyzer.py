#!/usr/bin/env python3
"""
Simple Text Analyzer - Day 20 (Fixed Version)
Handles NLTK data downloads automatically

Author: Manan (@MananCodes-dev)
Day: 20 of 100 Python CLI Tools Challenge
"""

import sys

def setup_nltk():
    """Download required NLTK data if missing"""
    try:
        import nltk
        # Try to download required data
        nltk.download('punkt', quiet=True)
        nltk.download('punkt_tab', quiet=True)
        nltk.download('brown', quiet=True)
        print("✅ NLTK data ready!")
        return True
    except Exception as e:
        print(f"Warning: Could not setup NLTK data: {e}")
        return False

def analyze_sentiment(text):
    """Check if text is positive, negative, or neutral"""
    try:
        from textblob import TextBlob
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        
        if polarity > 0.1:
            return "Positive 😊", polarity
        elif polarity < -0.1:
            return "Negative 😔", polarity
        else:
            return "Neutral 😐", polarity
    except Exception as e:
        print(f"Error in sentiment analysis: {e}")
        return "Unknown", 0

def count_words_simple(text):
    """Count words without TextBlob (backup method)"""
    words = text.split()
    return len(words)

def count_sentences_simple(text):
    """Count sentences without TextBlob (backup method)"""
    import re
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)

def count_words(text):
    """Count words in the text"""
    try:
        from textblob import TextBlob
        blob = TextBlob(text)
        return len(blob.words)
    except:
        return count_words_simple(text)

def count_sentences(text):
    """Count sentences in the text"""
    try:
        from textblob import TextBlob
        blob = TextBlob(text)
        return len(blob.sentences)
    except:
        return count_sentences_simple(text)

def main():
    print("📝 Simple Text Analyzer - Day 20")
    print("=" * 40)
    
    # Check if TextBlob is installed
    try:
        import textblob
        print("🤖 TextBlob found! Setting up...")
        setup_nltk()
    except ImportError:
        print("❌ TextBlob not found!")
        print("Install it with: pip install textblob")
        return
    
    # Get text from user
    if len(sys.argv) > 1:
        # If text provided as command line argument
        text = " ".join(sys.argv[1:])
    else:
        # Ask user for input
        text = input("Enter text to analyze: ")
    
    if not text.strip():
        print("No text provided!")
        return
    
    print(f"\nAnalyzing: '{text}'\n")
    
    # Do the analysis
    sentiment, score = analyze_sentiment(text)
    word_count = count_words(text)
    sentence_count = count_sentences(text)
    
    # Show results
    print("📊 RESULTS:")
    print(f"Sentiment: {sentiment}")
    if score != 0:
        print(f"Score: {score:.2f} (Range: -1 to 1)")
    print(f"Words: {word_count}")
    print(f"Sentences: {sentence_count}")
    
    if word_count > 0 and sentence_count > 0:
        avg_words = word_count / sentence_count
        print(f"Average words per sentence: {avg_words:.1f}")
    
    print(f"\n✅ Day 20 complete!")

if __name__ == "__main__":
    main()
