Attribute VB_Name = "TotalVol"
Sub total_volume()

Dim ws As Worksheet
For Each ws In Worksheets
ws.Activate

Cells(1, 9).Value = "Ticker"
Cells(1, 10).Value = "Volume Total"
    Dim Ticker As String
    Dim Vol As Double
    Vol = 0

    Dim Total_Vol As Double
    Total_Vol = 2

    Dim i As Long
        For i = 2 To 43398

            If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
            Ticker = Cells(i, 1).Value
            Vol = Vol + Cells(i, 7).Value
        
                Range("I" & Total_Vol).Value = Ticker
                Range("J" & Total_Vol).Value = Vol
            
            Total_Vol = Total_Vol + 1
            Vol = 0
    
         Else
        
            Vol = Vol + Cells(i, 7).Value
        
    End If
    
    Next i
    
Next ws

End Sub


