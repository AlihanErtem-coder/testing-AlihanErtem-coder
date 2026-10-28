Sinnvolle Tests:

Parse_time ():
Integer Rein -> Attribute Error PASST
Kein Doppelpunkt   -> Value error PASST
wie viele Nullen funktionerien z.B "09:01" oder "09:0000001" PASST
Stunde zwischen 0 und 23 + Minuten zwischen 0 und 59  -> Value Error PASST


Parse_measurement(line):
Line KEIN String -> Value Error PASST
genau Drei Felder-> Value Error PASST
mit ; getrennt-> Value Error
Leerzeichen weg PASST 
Stadt darf nicht leer sein-> Value Error PASST
float(21,7) -> Value Error PASST
KEINE Metorologische Prüfung



filter_by_temperature(measurements, lower, upper):

Grenzen sind Inklusive PASST
Reihenfolge Falsch-> AssertionError PASST
Identische Messungen -> Mehrmals PASST
