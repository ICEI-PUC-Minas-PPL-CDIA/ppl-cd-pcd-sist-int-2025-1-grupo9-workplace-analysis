![image](https://github.com/user-attachments/assets/7892a422-cf33-4911-a8e1-f788817a7feb)



<b>Descrição da Matrix:</b>

A matriz apresenta uma análise preditiva do etarismo no mercado de trabalho a partir da base de dados final. O processo começa com o carregamento e pré-processamento da base, criando uma variável alvo (etarismo) que identifica experiências negativas atribuídas à idade. Em seguida, são selecionadas variáveis relevantes e transformadas em categorias numéricas. Para lidar com o desbalanceamento da classe-alvo, a técnica SMOTE é aplicada, gerando amostras sintéticas que equilibram a base de dados. O modelo Random Forest foi treinado com 70% dos dados e testado com os 30% restantes. Após a otimização por GridSearchCV, o modelo alcançou uma acurácia de 77%. A matriz de confusão mostra que, entre os 1.911 casos analisados, 708 foram verdadeiros negativos e 759 verdadeiros positivos, enquanto 237 foram falsos positivos e 207 falsos negativos. Isso significa que aproximadamente 23% dos casos resultaram em erros de classificação, o que demonstra que, embora haja espaço para aprimoramento, os resultados são estatisticamente satisfatórios e bem distribuídos entre as classes.
