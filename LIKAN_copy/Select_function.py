
def Select_string():

	selectstring = "select s.id,s.SourceNo, s.date, vi.Quantity, c.Timevalue, c.tegund,i.Vendor,i.Vendor_name,i.description from sending s, Item_Category c,item i,vinnsla vi where c.name = i.Tegund and s.ItemNo = i.id and vi.itemno = i.id and s.RE_number = vi.Document_ID1 and s.date in('09/02/2018','12/02/2018','13/02/2018') order by s.id"

	return selectstring