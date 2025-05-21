import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Funzione principale
def main():
    st.image('Logo.png')  # TITLE and Creator information
    st.write('\n')  # add spacing
    st.markdown('Discover CloneCapital! Our platform offers proprietary algorithms to create synthetic futures contracts that mirror the performance of leading market indices with remarkable accuracy.')
    st.write('\n')  # add spacing
    
    # Espandi l'introduzione
    with st.expander("About CloneCapital"):
        st.write("""
            Founded in 2025 by four quantitative finance students from Politecnico di Milano, CloneCapital emerged from our shared vision to make sophisticated investment strategies accessible to everyone. Combining our academic expertise in financial modeling with a passion for technological innovation, we've created a platform that bridges the gap between institutional and retail investment capabilities.
              """)
        # Espandi l'obiettivo
    with st.expander("Our Solution"):
        st.write("""
            CloneCapital offers a unique way to invest in futures contracts that replicate the performance of key indices with unprecedented precision. Our proprietary algorithm enables investors to diversify their portfolios through synthetic positions that track market indices without the traditional barriers to entry. Experience the future of index investing—designed by students who understand both the mathematical complexities of financial markets and the need for intuitive investment solutions.
        """)
        # Espandi i rendimenti degli indici
    with st.expander("Introduction to the Indices"):
        st.markdown("""
        ### The indices we have focused on for replication are as follows:
        - **HFRX**: HFRX Global Hedge Fund Index, a widely followed benchmark representing the performance of hedge fund strategies across the industry.
        - **MSCI World**: MSCI World Index, tracking large and mid-cap equities across 23 developed markets worldwide.
        - **MSCI ACWI**: MSCI All Country World Index, capturing both developed and emerging market equities across a broad global universe.
        - **BBG Global Agg**: Bloomberg Global Aggregate Bond Index, a comprehensive benchmark for global investment-grade debt including government, corporate, and securitized bonds.
         """)
        st.write("Below is the plot showing the returns of the selected indices over time.")
        st.image("Logo.png")

    with st.expander("Overview of Asset Classes and Indices"):
        st.markdown("""
        ### The instruments used in our analysis include the following:

        - **RX1**: Highly liquid German government bond, considered a benchmark for fixed-income investments.
        - **TY1**: 10-year U.S. Treasury bond, representing a long-term, low-risk government debt instrument.
        - **GC1**: Gold, used as a store of value and a hedge against inflation and market volatility.
        - **CO1**: Price of Brent crude oil, a key global benchmark affected by geopolitical and market dynamics.
        - **ES1**: S&P 500 index, tracking 500 major U.S. companies across various sectors.
        - **VG1**: Euro Stoxx 50 index, representing 50 leading blue-chip stocks in the Eurozone.
        - **NQ1**: Nasdaq 100 index, composed mainly of large-cap technology and non-financial firms.
        - **TP1**: Topix index, reflecting the performance of Japanese stocks across multiple sectors.
        - **DU1**: 2-year German government bond ("Schatz"), a safe and liquid short-term investment.
        - **TU2**: 2-year U.S. Treasury bond, a short-term benchmark for risk-free government debt.
    """)

    # Espandi la scelta dell'indice da replicare
    with st.expander("Choose Index to Replicate"):
        selected_index = st.selectbox("Select an index to replicate", ["MSCI World AC", "MSCI World", "BB Global Bond Agg", "HFRX Index", "Monster Index 1", "Monster Index 2"])

        st.write(f"## Replication of {selected_index}")
        
        # Input per investment amount
        investment_amount = st.number_input("Enter the amount you want to invest in the selected index:", min_value=0.0, step=100.0)
        st.write("""Note that the replication portfolio might employ leverage or have a lower overall value
        """)
        st.write("""The weights are valid for the next 10 weeks and will be updated thereafter
        """)

        # Proporzioni di investimento nei futures 
        futures_allocation = {
            "MSCI World AC": {'CO1': 0.0658, 'DU1': 0, 'ES1': 0.4981, 'GC1': 0, 'NQ1': 0.0082, 'RX1': 0.2052, 'TP1': 0, 'TU2': 0, 'TY1': 0, 'VG1': 0},
            "MSCI World": {'CO1': 0.0931, 'DU1': 0, 'ES1': 0.4558, 'GC1': 0, 'NQ1': 0.0078, 'RX1': 0.2031, 'TP1': 0, 'TU2': 0, 'TY1': 0, 'VG1': 0},
            "BB Global Bond Agg": {'CO1': 0.0168, 'DU1': 0, 'ES1': 0, 'GC1': 0.2097, 'NQ1': 0.0059, 'RX1': 0.6707, 'TP1': 0, 'TU2': 0, 'TY1': 0, 'VG1': 0},
            "HFRX Index": {'CO1': 0.0782, 'DU1': 0.0790, 'ES1': 0.0513, 'GC1': 0.0467, 'NQ1': 0, 'RX1': 0.2697, 'TP1': 0.0673, 'TU2': 0.0660, 'TY1': 0.0713, 'VG1': 0},
            "Monster Index 1": {'CO1': 0.1044, 'DU1': 0, 'ES1': 0, 'GC1': 0, 'NQ1': 0.0508, 'RX1': 0.5973, 'TP1': 0, 'TU2': 0, 'TY1': 0, 'VG1': 0},
            "Monster Index 2": {'CO1': 0.1060, 'DU1': 0, 'ES1': 0.0867, 'GC1': 0, 'NQ1': 0.0518, 'RX1': 0.5355, 'TP1': 0, 'TU2': 0, 'TY1': 0, 'VG1': 0},
        }

        # Mean Turnover values per ogni indice 
        mean_turnover_values = {
            "MSCI World AC": 0.006,
            "MSCI World": 0.0077,
            "BB Global Bond Agg": 0.0022,
            "HFRX Index": 0.0036,
            "Monster Index 1": 0.0049,
            "Monster Index 2": 0.0056,
        }

        # Calcola l'investimento per ciascun future
        if investment_amount > 0:
            allocations = futures_allocation[selected_index]
            st.write("### Investment Allocation")
            for future_code, proportion in allocations.items():
                amount_invested = investment_amount * proportion
                st.write(f"*{future_code}:* {amount_invested:.2f}")

            

            # Mostra il grafico dei rendimenti dell'indice scelto e della replica
            if selected_index == "MSCI World AC":
                st.image("MXWO_LASSO_COMPARISON.png")
                st.write("Mean Tracking Error: 0.0224")
                st.write("Information Ratio: -0.8347")
            elif selected_index == "MSCI World":
                st.image("MXWD_LASSO_PREDICTION.png")
                st.write("Mean Tracking Error: 0.0352")
                st.write("Information Ratio: -0.3977")
            elif selected_index == "BB Global Bond Agg":
                st.image("LEGATRUU_LASSO_PREDICTION.png")
                st.write("Mean Tracking Error: 0.0366")
                st.write("Information Ratio: 0.0964")
            elif selected_index == "HFRX Index":
                st.image("HFRLX_ELASTIC_COMPARISON.png")
                st.write("Mean Tracking Error: 0.0158")
                st.write("Information Ratio: -0.3074")
            elif selected_index == "Monster Index 1":
                st.image("MONSTER1_LASSO_PREDICTION.png")
                st.write("Mean Tracking Error: 0.0243")
                st.write("Information Ratio: -0.6899")
            elif selected_index == "Monster Index 2":
                st.image("MONSTER2_LASSO_COMPARISON.png")
                st.write("Mean Tracking Error: 0.030")
                st.write("Information Ratio: -0.485")

            # Calcola e mostra il "Mean Turnover" moltiplicato per l'importo investito
            mean_turnover = mean_turnover_values[selected_index] * investment_amount
            st.write(f"Mean Turnover: {mean_turnover:.2f}")

            # Spiegazione breve dei termini
            st.write("\n")
            st.write("Mean Tracking Error: Measures the deviation of the replication portfolio's returns from the target index's returns.")
            st.write("Information Ratio: Indicates the risk-adjusted return of the replication portfolio compared to the target index.")
            st.write("Mean Turnover: Represents the average proportion of the portfolio that is traded over a given period.")


if __name__ == "__main__":
    main()
