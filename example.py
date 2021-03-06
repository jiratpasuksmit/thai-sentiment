# -*- coding: utf-8 -*-

from thai_sentiment import Tokenizer

import time

if __name__ == '__main__':
    start_time = time.time()
    print("|".join(Tokenizer().tokenize('มานานเกินกว่า 4 ปีแล้ว')))
    print("|".join(Tokenizer().tokenize('ปวดหัวคงจะเป็นอาการที่มนุษย์รู้สึกบ่อยที่สุดในบรรดาอาการทั้งหลายเพราะหัวอยู่ใกล้สมองอันเป็นที่รับรู้ ที่จริงอาการอื่นๆ มันก็คงจะมีมากเหมือนกัน เช่น ปวดแข้ง ปวดขา ปวดนิ้วเท้า แต่เนื่องจากมันอยู่ไกลที่รับรู้ จึงไม่ค่อยคำนึงถึง ปวดหัวเกือบทั้งหมดเกิดจากอาการเครียด เช่น อดนอน ทำงานใช้ความคิดมาก มีอารมณ์ เช่น รถติด วิตกกังวล โกรธ เกลียด รถไฟฟ้า')))
    print("|".join(Tokenizer().tokenize('ประเทศไทยมีบริการเทเลเท็กซ์โดยไม่คิดมูลค่าทางช่อง 5 มานานเกินกว่า 4 ปีแล้ว')))
    print("|".join(Tokenizer().tokenize('เทเลเท็กซ์ kbank มานาน')))
    print("|".join(Tokenizer().tokenize('อยากสอบถามคุณผู้หญิงหน่อยครับ ทำไมคนที่รักกันมา 5 ปีถึงเลิกกันง่ายๆทั้งๆที่แทบไม่เคยทะเลาะกันเลย')))
    print("|".join(Tokenizer().tokenize('เขาไปช้อปปิ้งที่คาร์ฟูร์แผนกซูเปอร์มาร์เก็ตและไปกินข้าวที่แมคโคร')))
    print("|".join(Tokenizer().tokenize("ลองเทสสินค้าใหม่")))
    print("|".join(Tokenizer().tokenize("เมื่อยามนี้ไ")))
    print("|".join(Tokenizer().tokenize('แชร์ประสบการณ์ถูกพนักงานแบงค์เขียวรูดบัตรเครดิตไปเกือบล้านบาท')))
    print("--- %s seconds ---" % (time.time() - start_time))
