DATEADD(
    DAY,
    COALESCE(
        TRY_CAST(
            TRIM(SUBSTRING(
                QuoteConfiguration.[Name], 
                CHARINDEX(', ', QuoteConfiguration.[Name]) + 2, 
                CHARINDEX(' Days', QuoteConfiguration.[Name]) - CHARINDEX(', ', QuoteConfiguration.[Name]) - 2
            )) AS INT
        ),
        30
    ),
    CustomerQuote.EffectiveDate
)
