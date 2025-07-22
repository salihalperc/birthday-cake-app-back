from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS

app = Flask(__name__)
SECRET_PASSWORD = os.getenv("SECRET_PASSWORD")

CORS(app, origins=["https://salihalperc.github.io"])
@app.route('/verify-password', methods=['POST'])
def verify_password():
    data = request.get_json()
    if data.get('password') == SECRET_PASSWORD:
        return jsonify({"success": True})
    return jsonify({"success": False})

@app.route('/get-message', methods=['GET'])
def get_message():
    return jsonify({
        "message": """Sevgili Eşim, 

Bugün senin, eşimin, çocuklarımın annesi olması için dua ettiğim kişinin doğum günü. İyi ki doğmuş, iyi ki hayatıma girmiş ve o hayatı renklendirmişsin. Sana karşı içimde beslediğim sevgiyi nasıl ifade etsem bilmiyorum fakat umarım sana layık kelimeler çıkar kalemimden. Seni her şeyinle çok seviyorum. Akıllı olmanla, zorda kaldığımda bana yol göstermenle, beni hep kendinden bile önce tutmanla önemsemenle, hatta farkında olmasan da sinirlendiğinde ve daraldığında bile o durumda seni gözlemleyip seni seviyorum. Kızgın, üzgün veya darda olman tabii ki beni mutlu etmiyor, aslında seni çok sevdiğim için senin kızgın, dertli ve stresli olarak gördüğün hallerin bile benim sevgimin bir parçası haline gelmiş. Çünkü seni kendimden bile çok seviyorum. Seninle beraber neredeyse 2 koca sene geçirdik. Rabbimden isteğim daha huzurlu nicelerini geçirmemiz, daha da büyük bir aile olmamız, hayırlı evlatlar yetiştirebilmemiz. Çünkü eminim ki anne olmak en çok sana yakışacak. Geriye dönüp baktığımda hayatımızdaki bir çok şeyin bizi nasıl karşılaştırdığını görüyorum ve diyorum ki bence bunca şey boşa değil. Senin dershanen ve sonrasında işe girmen benim ucu ucuna bir tercihle Ankarayı tutturmam. Benim takıcıya gitmeme sebep olan arkadaşlarımın da Ankarada olmaları. Normalde hiç yapmadığım ve yapamayacağım bir şekilde tanışmaya çalışmam mesela, ki bence çok şaşırtıcı. Bütün bunları ve hatta daha fazlasını düşündüğümde diyorum ki inşallah bunları beraber daha çok anarız, gülerek mutlu bir şekilde anlatırız. Çünkü ben bunu çok istiyorum, seninle bir aile kurmayı (gönül bağı olarak zaten aile olarak görsem de ) ikimizin de birbirini mutlu ettiği, zor zamanlarına destek olduğu bir aile kurmayı. Öyle ki bu satırları yazarken hayalini kurdurup gözlerimi dolduracak kadar. Öyle ki, yüzündeki en ufak bir tebessüm bile dolu kafamı temizliyor, tüm yorgunluğumu alıp beni dinginleştiriyor. Öyle ki, sana olan sevgim her geçen gün çığ gibi büyüyor. Hani insan sevdiği için bulduğu en güzel şeyleri biriktirir saklar ya, ben de aynı öyle sana duyduğum sevdayı büyütüp saklıyorum gönlümde. Ve en çok da sarılıp kalplerimiz birbirimizi tamamladığında o sevda adeta depreme dönüşüyor. Adı sevda da olsa, gönülde de saklansa anlıyor sevgilisini ve engin bir deniz gibi coşuyor. Geçirdiğimiz onca zamanı düşünüyorum sevgilim, beraber atlattığımız çözdüğümüz sorunları, ki eminim dahasını da çözeceğiz atlatacağız bazen de elimizde olmayan şeyleri çözemeyip sadece alışacağız. Gönlümün isteği şu ki, hayat bi su gibi akıp giderken biz hep birbirimize saygı ve sevgi dolu olalım, birbirimize ve ailemize arka çıkalım. Bu yazıyı nasıl yazacağım ve sana olan sevgimi nasıl daha iyi ifade edebilirim diye çok düşündüm. Umarım ki şu an gözlerimin dolu olması iyi bir şekilde ifade edebildiğimin göstergesidir. İyi ki varsın, iyi ki doğdun, iyi ki benim oldun, iyi ki kader bizim için ağlarını örmüş güzelim. Seni çookkkkk seviyorummmmm güzel eşim. Allah seni benden ve gönlümden ayırmasın, birlikte nice doğum günlerine, doğum günün kutlu olsun güzelim🤍❤️"""
    })

# ⛔ app.run() KULLANMA! Gunicorn kullanacağız.
