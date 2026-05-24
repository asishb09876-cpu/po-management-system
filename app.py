import streamlit as st
    total_excise = po_df['total_excise'].sum()
    total_invoice = po_df['invoice_value'].sum()
    total_vat = po_df['vat'].sum()
    total_tcs = po_df['tcs'].sum()

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    kpi1.metric('Total Excise', f'₹ {total_excise:,.2f}')
    kpi2.metric('Total Invoice', f'₹ {total_invoice:,.2f}')
    kpi3.metric('Total VAT', f'₹ {total_vat:,.2f}')
    kpi4.metric('Total TCS', f'₹ {total_tcs:,.2f}')

    st.divider()

    # =========================
    # MONTHLY EXCISE CHART
    # =========================
    monthly_excise = po_df.groupby('month')['total_excise'].sum().reset_index()

    fig_excise = px.bar(
        monthly_excise,
        x='month',
        y='total_excise',
        title='Monthly Excise Duty'
    )

    st.plotly_chart(fig_excise, use_container_width=True)

    # =========================
    # PRODUCT WISE SALES
    # =========================
    product_sales = po_df.groupby('product_name')['invoice_value'].sum().reset_index()

    fig_product = px.pie(
        product_sales,
        names='product_name',
        values='invoice_value',
        title='Product Wise Invoice Value'
    )

    st.plotly_chart(fig_product, use_container_width=True)

    # =========================
    # MONTHLY INVOICE VALUE
    # =========================
    monthly_invoice = po_df.groupby('month')['invoice_value'].sum().reset_index()

    fig_invoice = px.line(
        monthly_invoice,
        x='month',
        y='invoice_value',
        markers=True,
        title='Monthly Invoice Value'
    )

    st.plotly_chart(fig_invoice, use_container_width=True)

# =========================
# CLOSE CONNECTION
# =========================
conn.close()
