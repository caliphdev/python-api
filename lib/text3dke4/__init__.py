from PIL import Image, ImageDraw, ImageFont

class tulis:
    """
    listOrText : String
    """
    def __init__(self, listOrText):
        self.text = listOrText
        self.output = []
    def tulis(self):
        img, font, kata, tempkata=Image.open("lib/text3dke4/babu.jpg"), ImageFont.truetype("lib/text3dke4/Optimal3d.ttf",45),'',''
        draw=ImageDraw.Draw(img)
        if type(self.text) is not list:
            self.output=[]
            for i in self.text:
                if draw.textsize(tempkata, font)[0] < 505:
                    tempkata+=i
                else:
                    kata, tempkata=kata+'%s\n'%tempkata, i
            if tempkata:
                kata+="%s"%tempkata
            spliter=kata.split("\n")
        else:
            spliter=self.text
        line=125
        for i in spliter[:56]:
            draw.text((70, int(line)), i, font=font, fill=("white")) #selisih = Line
            line+=85 + 4.0
        self.output.append(img)
        if len(spliter) > 56:
            self.output+=tulis(spliter[56:]).tulis()
        return self.output
    def __repr__(self):
        return "<length: %s char>"%len(self.text)
