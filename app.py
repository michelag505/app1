import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.image('Logo_1.png')  
    st.write('\n')  
    st.markdown('Discover CloneCapital! Our platform offers proprietary algorithms to create synthetic futures contracts that mirror the performance of leading market indices with remarkable accuracy.')
    st.write('\n')  
    
    # Expand intro
    with st.expander("About CloneCapital"):
        st.write("""
            Founded in 2025 by four quantitative finance students from Politecnico di Milano, CloneCapital emerged from our shared vision to make sophisticated investment strategies accessible to everyone. Combining our academic expertise in financial modeling with a passion for technological innovation, we've created a platform that bridges the gap between institutional and retail investment capabilities.
              """)
        # objective
    with st.expander("Our Solution"):
        st.write("""
            CloneCapital offers a unique way to invest in futures contracts that replicate the performance of key indices with unprecedented precision. Our proprietary algorithm enables investors to diversify their portfolios through synthetic positions that track market indices without the traditional barriers to entry. Experience the future of index investing—designed by students who understand both the mathematical complexities of financial markets and the need for intuitive investment solutions.
        """)
        # indexes
    with st.expander("Overview of the Indices"):
        st.markdown("""
        ### We base our replication strategy on the following indices:
        - **HFRX**: HFRX Global Hedge Fund Index, a widely followed benchmark representing the performance of hedge fund strategies across the industry.
        - **MSCI World**: MSCI World Index, tracking large and mid-cap equities across 23 developed markets worldwide.
        - **BBG Global Agg**: Bloomberg Global Aggregate Bond Index, a comprehensive benchmark for global investment-grade debt including government, corporate, and securitized bonds.
        - **MonsterIndex 1**: Custom index constructed as a weighted linear combination of the listed indices, using weights [1/3, 1/3, 1/3], offering a diversified investment opportunity.
        - **MonsterIndex 2**: Custom index constructed as a weighted linear combination of the listed indices, using weights [0.25, 0.5, 0.25], offering a diversified investment opportunity.
         """)
        st.write("The chart below visualizes how the returns of the indices have evolved over time.")
       
        st.image("indici.png")

    with st.expander("Overview of the Futures used in the Replication Portfolio"):
        st.markdown("""

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
        st.write("The chart below visualizes the futures used in the replicating portfolio.")
        st.image("futures55.png")

    # choose index
    with st.expander("Choose Index to Replicate"):
        selected_index = st.selectbox("Select an index to replicate", [ "MSCI World", "BB Global Bond Agg", "HFRX Index", "Monster Index 1", "Monster Index 2"])

        st.write(f"## Replication of {selected_index}")
        
        # investment amount
        investment_amount = st.number_input("Enter the principal you want to invest:", min_value=0.0, step=100.0)
        st.write(""" The proposed allocation is valid for a week and will be updated afterwards
        """)

        # futures ptf
        futures_allocation = {
            "MSCI World": {'RX1': 0.006481,'TY1': -0.025120,'GC1': 0.069007,'CO1': 0.009169,'ES1': 0.427432,'VG1': 0.157822,'NQ1': 0.152566,'TP1': 0.122028,'DU1': 0.002261,'TU2': -0.001807},
            "BB Global Bond Agg": {'RX1': 0.141810,'TY1': 0.198919,'GC1': 0.113667,'CO1': -0.025174,'ES1': 0.062915,'VG1': -0.066337,'NQ1': 0.004592,'TP1': 0.031359,'DU1': 0.039291,'TU2': -0.005474},
            "HFRX Index": { 'RX1': 0.140715,'TY1': 0.204072,'GC1': -0.010062,'CO1': 0.008248,'ES1': 0.067675,'VG1': -0.051717,'NQ1': 0.021788,'TP1': 0.119898,'DU1': 0.066198,'TU2': -1.688163},
            "Monster Index 1": {'RX1': 0.080728,'TY1': -0.003102,'GC1': 0.080825,'CO1': 0.000983,'ES1': 0.229590,'VG1': -0.012376,'NQ1': 0.054494,'TP1': 0.080853,'DU1': 0.011704,'TU2': 0.000087},
            "Monster Index 2": { 'RX1': 0.065566,'TY1': -0.009756,'GC1': 0.081312,'CO1': 0.002029,'ES1': 0.281891,'VG1': 0.036103,'NQ1': 0.080437,'TP1': 0.095376,'DU1': 0.009152,'TU2': -0.000760},
        }


        # investment amount
        if investment_amount > 0:
            allocations = futures_allocation[selected_index]
            st.write("### Investment Allocation")
            for future_code, proportion in allocations.items():
                amount_invested = investment_amount * proportion
                st.write(f"*{future_code}:* {amount_invested:.2f}")


            # replication
            if selected_index == "MSCI World":
                st.image("MSCIworld.png")
                st.write("Tracking Error: 3.81%")
                st.write("Information Ratio: 0.01")
            elif selected_index == "BB Global Bond Agg":
                st.image("LEGATURUU.png")
                st.write("Tracking Error: 3.80%")
                st.write("Information Ratio: -0.04")
            elif selected_index == "HFRX Index":
                st.image("HFRX.png")
                st.write("Tracking Error: 4.72%")
                st.write("Information Ratio: -0.77")
            elif selected_index == "Monster Index 1":
                st.image("MonsterIndex1.png")
                st.write("Tracking Error: 3.34%")
                st.write("Information Ratio: -0.13")
            elif selected_index == "Monster Index 2":
                st.image("MonsterIndex2.png")
                st.write("Tracking Error: 3.33%")
                st.write("Information Ratio: -0.03")

        

            # metrics
            st.write("\n")
            st.write("Tracking Error: Quantifies how closely the replication portfolio follows the benchmark index by measuring the standard deviation of the difference in their returns over time.")
            st.write("Information Ratio: Evaluates the performance of the replication portfolio relative to the benchmark by dividing the excess return by the tracking error, reflecting how efficiently the portfolio generates active returns.")

if __name__ == "__main__":
    main()
