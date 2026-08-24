import bibtexparser
import spacy
from collections import Counter

# Load the local spaCy English model
nlp = spacy.load("en_core_web_sm")

def generate_keywords_local(title, abstract, top_n=5):
    # Combine title and abstract for a full picture
    text = f"{title}. {abstract}"
    doc = nlp(text)
    
    keywords = []
    
    # 1. Extract Named Entities (like specific technologies, organizations, places)
    # Excluding dates, cardinal numbers, etc.
    excluded_entities = {"DATE", "TIME", "PERCENT", "MONEY", "QUANTITY", "CARDINAL", "ORDINAL"}
    for ent in doc.ents:
        if ent.label_ not in excluded_entities:
            keywords.append(ent.text.strip().lower())
            
    # 2. Extract Noun Chunks (e.g., "machine learning", "neural network")
    for chunk in doc.noun_chunks:
        # Clean up determiners (like 'a', 'the') and long phrase clutter
        clean_chunk = " ".join([token.text for token in chunk if not token.is_stop and not token.is_punct])
        if clean_chunk and len(clean_chunk.split()) <= 3:  # Keep tags between 1 and 3 words
            keywords.append(clean_chunk.lower())
            
    # Filter out empty strings or single character artifacts
    keywords = [k for k in keywords if len(k) > 2]
    
    # Count frequencies and grab the most common unique keywords
    most_common = [word for word, count in Counter(keywords).most_common(top_n)]
    
    # Capitalize the first letter of each keyword for clean tags
    formatted_keywords = [k.title() for k in most_common]
    
    return ", ".join(formatted_keywords) if formatted_keywords else "General"

# Load your existing BibTeX file
with open('publications.bib', 'r', encoding='utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Iterate through each publication entry
for entry in bib_database.entries:
    title = entry.get('title', '')
    abstract = entry.get('abstract', '')
    
    if abstract or title:
        print(f"Processing locally: {title[:50]}...")
        # Automatically generate and inject the keywords field
        entry['keywords'] = generate_keywords_local(title, abstract)

# Save the updated詳 BibTeX file
with open('publications_with_keywords.bib', 'w', encoding='utf-8') as bibtex_file:
    bibtexparser.dump(bib_database, bibtex_file)

print("Local automation complete! Check 'publications_with_keywords.bib'")
