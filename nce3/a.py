N = 60
import os
al = xrange(301,301+N)
for i in al:
    print '''           <tr>
              <td><a href="%d.html">Lesson %02d</a><td>
           </tr>'''%(i,i-300)
