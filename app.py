import streamlit as st
from news_scraper import get_related_articles
from summarizer import summarize_article
from fake_check import analyze_verdict

if "history" not in st.session_state:
    st.session_state.history = []

st.title("🧠 Fake News Debunker")

headline = st.text_input("Enter a News Headline")

if st.button("Check Authenticity"):
    if not headline.strip():
        st.warning("Please enter a headline.")
    else:
        st.info("Fetching related articles...")
        articles = get_related_articles(headline)

        if not articles:
            st.error("No related articles found.")
        else:
            st.success(f"Found {len(articles)} articles")
            summaries = [summarize_article(a['text']) for a in articles[:3]]
            verdict = analyze_verdict(headline, summaries)
            st.session_state.history.append({
            "headline": headline,
            "verdict": verdict,
            "sources": [a['url'] for a in articles[:3]]
            })


            for i, (a, summary) in enumerate(zip(articles, summaries), 1):
                st.markdown(f"### Article {i}")
                st.write(f"🔗 [{a['title']}]({a['url']})")
                st.write("📝 Summary:")
                st.info(summary)

            st.markdown("---")
            st.subheader("🧾 Final Verdict")
            st.success(verdict)
with st.sidebar:
    st.header("🕘 History")
    if st.session_state.history:
        for item in reversed(st.session_state.history[-5:]):  # Show last 5 entries
            st.markdown(f"**Headline:** {item['headline']}")
            st.markdown(f"**Verdict:** {item['verdict']}")
            for i, url in enumerate(item["sources"], 1):
                st.markdown(f"[Source {i}]({url})")
            st.markdown("---")
    else:
        st.info("No checks yet.")

