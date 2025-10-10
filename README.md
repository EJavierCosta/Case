# 🚀 Business Case - Engenharia de Dados (Gocase/Gogroup)

## Visão Geral do Projeto
Este projeto simula a estruturação inicial da área de Dados de um e-commerce B2C de alto crescimento (Gocase/Gogroup), focando na automação da ingestão e na geração de *insights* estratégicos para os times de Vendas e Supply Chain.

A solução utiliza uma **arquitetura moderna e escalável**, combinando um orquestrador leve (*n8n*) com um motor de processamento de Big Data (*PySpark*).

---

## 🛠️ Arquitetura e Tecnologia (Stack)

| Componente | Ferramenta | Propósito Estratégico |
| :--- | :--- | :--- |
| **Orquestração & Workflow** | **n8n** | Automação e agendamento de ponta a ponta (disparo do *job* e envio de relatório). |
| **Processamento de Dados** | **PySpark** | Processamento eficiente do alto volume de dados, garantindo escalabilidade. |
| **Fonte de Dados** | Google Drive (Simulação) | Local de onde os CSVs brutos são ingeridos. |
| **Gerenciamento de Estado** | **n8n Data Store** | Armazenamento persistente da **Marca D'água (HWM)**, garantindo a ingestão incremental (simulação de CDC). |
| **Metadados & Logs** | Python/Logbook | Coleta do `MAX(ID)` e geração de logs do PySpark. |

---

## ⚙️ Fluxo de Trabalho Automatizado (n8n Pipeline)

O *workflow* é projetado para rodar semanalmente e processar apenas as novas linhas de dados, otimizando o tempo de execução (Marca D'água).

1.  **START (Trigger Agendado):** O n8n é acionado.
2.  **GET HWM (Data Store):** O valor da última `Marca D'água (Ex: MAX(id_pedido))` é lido do Data Store.
3.  **INGESTÃO E PROCESSAMENTO (PySpark Job):** Um *script* PySpark é executado (simulado em ambiente local/Cloud), recebendo o HWM.
    * **Filtragem Incremental:** O PySpark lê os CSVs do Google Drive e filtra as linhas onde o `id_pedido` ou `id_produto` é **maior** que o HWM.
    * **Análise:** Realiza as transformações, cruzamentos e cálculos de KPIs.
    * **Geração de Relatório:** Cria gráficos e resumo de *insights*.
    * **Novo HWM:** Calcula o novo `MAX(ID)` dos dados processados.
4.  **SET HWM (Data Store):** O n8n recebe o novo valor do HWM e o armazena no Data Store, fechando o ciclo incremental.
5.  **REPORTING (E-mail/PDF):** O n8n anexa o relatório em PDF e o envia aos *stakeholders* (Vendas e Supply Chain).

---

## 📊 Principais Insights e Conclusões

A análise focou em transformar os desafios de negócio (rupturas, oscilações de vendas, problemas logísticos) em métricas acionáveis, demonstrando como a Engenharia de Dados apoia o crescimento (Ponta Firme e Amor pelo Cliente).

### 1. Vendas & Conversão

* **Sazonalidade e Previsão:** [Insira a conclusão principal sobre picos de venda e como eles devem ser previstos].
* **Otimização de Promoção:** [Insira a conclusão sobre o AOV e a lucratividade de descontos; por exemplo, se os descontos precisam ser mais focados em *kits*].

### 2. Supply Chain & Estoque

* **Risco de Receita:** [Insira a métrica de "Receita Potencial Perdida" devido às rupturas nos Top N produtos].
* **Gargalos:** [Insira a conclusão sobre o desvio de tempo de reposição nos fornecedores/categorias mais lentas].

### 3. Logística & Entregas

* **Impacto no Cliente:** [Insira a correlação entre atrasos e a taxa de cancelamento de pedidos, destacando o impacto na satisfação do cliente].
* **Problemas Recorrentes:** [Insira as regiões/categorias com a maior incidência de atrasos].

---

## ⭐ Recomendações Estratégicas para Otimização

1.  **Implementação de Monitoramento em *Streaming* (Kafka/PySpark):** Para mitigar rupturas de estoque em tempo quase real, o próximo passo deve ser migrar a ingestão dos CSVs para um *stream* Kafka.
2.  **Criação de Alertas Automatizados:** O *workflow* no n8n deve ser expandido para enviar alertas imediatos via Slack ou e-mail quando a métrica de **Estoque Crítico** (calculada pelo PySpark) for violada.
3.  **Versionamento do Código:** Sugestão de migrar todos os arquivos JSON do n8n e scripts PySpark para um repositório **Git/GitHub** para facilitar a colaboração e a **Transparência Máxima** do Time Campeão.

---
