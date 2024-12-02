DATEADD(
    DAY,
    COALESCE(
        CASE
            WHEN CHARINDEX(', ', QuoteConfiguration.[Name]) > 0 
                 AND CHARINDEX(' Days', QuoteConfiguration.[Name]) > CHARINDEX(', ', QuoteConfiguration.[Name])
            THEN CAST(
                TRIM(SUBSTRING(
                    QuoteConfiguration.[Name], 
                    CHARINDEX(', ', QuoteConfiguration.[Name]) + 2, 
                    CHARINDEX(' Days', QuoteConfiguration.[Name]) - CHARINDEX(', ', QuoteConfiguration.[Name]) - 2
                )) AS INT
            )
            ELSE NULL
        END,
        30
    ),
    CustomerQuote.EffectiveDate
)
