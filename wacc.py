def WACC(sharePrice,sharesOutstanding,netDebt,costDebt,costEquity,taxRate):
    # costEquity = rf + [B * (rm-rf)]
    equity = sharePrice*sharesOutstanding
    total = equity+netDebt
    return (equity/total)*costEquity+(netDebt/total)*costDebt*(1-taxRate)
print(WACC(273.52,4471.5,-98769,.0175,.073,.1730))