# Working of these application
A Streamlit web app that lets you upload documents (PDF, Word, TXT) and run text analysis operations like:

-> Word Cloud
-> Word Frequency (Bar Chart)
-> Bigrams 
The app extracts text from uploaded files, processes it, and shows results as interactive visualizations.

# 📊 Visualization Details
✅ Word Cloud
- Highlights word prominence visually.
- Great for spotting dominant themes or keywords.
✅ Frequency Bar Chart
- Shows exact word counts.
- Useful for analytical comparison of word usage.
✅ Bigram Bar Chart
- Reveals common phrases or word pairings.
- Adds context beyond single-word frequency.

# used libraries
- Streamlit – for building the interactive web app
- pdfplumber – to extract text from PDF files
- python-docx – to extract text from Word (.docx) files
- matplotlib – for plotting bar charts and word clouds
- wordcloud – to generate word cloud visuals
- collections.Counter – to count word and bigram frequencies
- io – to handle file byte streams
- pandas – imported but not used in this version
