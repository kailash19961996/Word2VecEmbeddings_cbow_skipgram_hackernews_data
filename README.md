# Word2Vec Embeddings from Scratch for Hacker News Data

In this project, I have implemented the CBOW (Continuous Bag-of-Words) and Skip-Gram architectures of the Word2Vec algorithm from scratch to generate word embeddings for the Hacker News dataset. These embeddings were then used to predict scores for Hacker News posts.


https://github.com/kailash19961996/Word2VecEmbeddings_cbow_skipgram_hackernews_data/assets/123597753/c711a983-e004-4773-b07a-3091dbc10a8c


## Key Features
1. **CBOW and Skip-Gram Word2Vec Implementations**: I have developed the CBOW and Skip-Gram models using PyTorch, without relying on pre-built Word2Vec libraries.
2. **Hacker News Dataset Preprocessing**: The project includes thorough preprocessing of the Hacker News dataset, including text cleaning, tokenization, and vocabulary building.
3. **Word Embedding Training and Evaluation**: The trained word embeddings are evaluated on their ability to predict the scores of Hacker News posts, demonstrating their effectiveness in capturing semantic and syntactic relationships.

## Challenges Addressed
1. **CBOW and Skip-Gram Implementations**: Implementing the core algorithms of the CBOW and Skip-Gram models, including the training objective functions and the negative sampling process, was a key challenge.
2. **Hacker News Data Preprocessing**: Handling the complexities of the Hacker News dataset, such as dealing with HTML tags, URLs, and irregular text formatting, required careful attention.
3. **Model Evaluation and Optimization**: Determining the optimal hyperparameters for the Word2Vec models and the downstream prediction task, as well as developing suitable evaluation metrics, was crucial for achieving high performance.

## Future Improvements
1. **Exploring Advanced Word Embedding Techniques**: Investigating more recent word embedding models, such as #GloVe or #FastText, to further enhance the performance and capabilities of the system.
2. **Incorporating Additional Data Sources**: Expanding the dataset by incorporating other online communities or forums related to Hacker News, to enrich the word embeddings and improve the prediction accuracy.
3. **Multilingual Support**: Extending the project to handle multiple languages, allowing for a more diverse and inclusive user experience.
4. **Integration with Other Applications**: Exploring ways to integrate the Word2Vec embeddings and the prediction model into other applications, such as content recommendation systems or search engines.

## Acknowledgments
I would like to acknowledge the pioneering work of the Word2Vec authors, Tomas Mikolov et al., whose research and algorithms have been instrumental in this project. Additionally, I'm grateful for the open-source tools and libraries that have made this project possible, including PyTorch, Streamlit, and the various natural language processing resources available.
