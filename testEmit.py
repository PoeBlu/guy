#!/usr/bin/python
# -*- coding: utf-8 -*-
import guy,asyncio,datetime

class Emit(guy.Guy):
    size=(300,300)
    test="HELLO"
    __doc__="""
<<test>>
<script>
guy.on("view",function(a,b) {
    document.body.innerHTML+= (a+b)+"<br>";
})

</script>
<button onclick="self.emitMe('view',42,43)">emit</button>
<button onclick="self.emit  ('view',42,43)">emit glob</button>
<hr/>
    """


if __name__ == "__main__":
    Emit( ).run()


