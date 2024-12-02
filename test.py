CASE WHEN (CASE 
    WHEN CHARINDEX(', ', QuoteConfiguration.[Name]) > 0 AND CHARINDEX(' Days', QuoteConfiguration.[Name]) > CHARINDEX(', ', QuoteConfiguration.[Name])
    THEN CAST(
        TRIM(SUBSTRING(
                QuoteConfiguration.[Name], 
                CHARINDEX(', ', QuoteConfiguration.[Name]) + 2, 
                CHARINDEX(' days', QuoteConfiguration.[Name]) - CHARINDEX(', ', QuoteConfiguration.[Name]) - 2
            )
        ) AS INT
    )
    ELSE NULL
END)is NULL  THEN DATEADD(DAY,30,CustomerQuote.EffectiveDate)
ELSE DATEADD(DAY,    (CASE 
    WHEN CHARINDEX(', ', QuoteConfiguration.[Name]) > 0 AND CHARINDEX(' Days', QuoteConfiguration.[Name]) > CHARINDEX(', ', QuoteConfiguration.[Name])
    THEN CAST(
        TRIM(
            SUBSTRING(
                QuoteConfiguration.[Name], 
                CHARINDEX(', ', QuoteConfiguration.[Name]) + 2, 
                CHARINDEX(' days', QuoteConfiguration.[Name]) - CHARINDEX(', ', QuoteConfiguration.[Name]) - 2
            )
        ) AS INT
    )
    ELSE NULL
END),CustomerQuote.EffectiveDate) 
