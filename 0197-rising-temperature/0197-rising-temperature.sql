select w.id from 
weather w join weather k 
on subdate(w.recorddate,1)=k.recorddate 
and w.temperature>k.temperature; 
