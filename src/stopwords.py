def get_stopwords(words):
    """Detect language used in chat then return corresponding stopwords."""
    d = {lang: len(stopwords.intersection(words)) for lang, stopwords in STOPWORDS.items()}
    lang_used = max(d, key=d.get)
    return STOPWORDS[lang_used]

STOPWORDS = {
    'en': {
		# get from default wordcloud stopwords with additional stopwords
        'above','up','at','own','i','my','of','those',"where's",'yourselves','each','has','while','in',
        'your','r','having',"they'd","we'd",'same','also','did','them',"wasn't","don't",'here','herself',
        'all','itself','an','cannot','doing',"she'll",'some',"she'd",'then','during','his','over',
        'yourself',"we'll",'nor','have','its',"shouldn't",'off','being',"you've",'ours','for','only',
        'their','than',"you'll",'hers','he',"you're",'further','which',"here's","who's",'both',"why's",
        'could','down',"mustn't",'again',"let's",'from',"weren't",'would','theirs',"doesn't",'ourselves',
        "she's",'through','himself','ought','against','how',"we've","i'll",'very','get',"he'd",'who',"i'd",
        'should','can','what','do','under',"aren't",'been','our','few',"he's",'http',"won't",'after',
        "they're",'where',"hadn't",'but',"i've",'www','she','therefore','had','is',"hasn't","it's",'we',
        'him','about','otherwise','themselves',"wouldn't","i'm","can't",'yours','since','such',"couldn't",
        "what's",'you','and','because',"didn't",'if','before','a',"shan't","you'd",'into','any','by','so',
        'between','once',"they'll",'com','the','more','me','why','or',"he'll",'until','other','was','no',
        "they've",'does',"that's","there's","when's",'ever','be',"haven't",'however','out','am','k','these',
        'are','else','her','it','that','with','there','hence','like','they','on','below','myself','not','to',
        "we're","isn't",'most','too','were','when','just',"how's",'as','this','whom','shall','u','ok','o','oh',
        'ha','haha','hahaha', 'hahahaha''hoho','hi'},

    'in': {
		# combine from https://github.com/har07/PySastrawi and https://github.com/indonesia/ID-Stopwords with additional stopwords
        'a','abis','ad','ada','adalah','adanya','adapun','agak','agaknya','agar','ah','ahaha','ahahaha',
        'ahahahaha''aj','aja','akan','akankah','akhir','akhiri','akhirnya','aku','akulah','amat','amatlah',
        'anda','andalah','antar','antara','antaranya','apa','apaan','apabila','apakah','apalagi','apatah',
        'arti','artinya','asal','asalkan','atas','atau','ataukah','ataupun','ato','awal','awalnya','b','bagai',
        'bagaikan','bagaimana','bagaimanakah','bagaimanapun','bagainamakah','bagi','bagian','bahkan','bahwa',
        'bahwasannya','bahwasanya','baik','baiklah','bakal','bakalan','balik','banget','banyak','bapak',
        'baru','bawah','beberapa','begini','beginian','beginikah','beginilah','begitu','begitukah',
        'begitulah','begitupun','bekerja','belakang','belakangan','belom','belum','belumlah','benar',
        'benarkah','benarlah','berada','berakhir','berakhirlah','berakhirnya','berapa','berapakah',
        'berapalah','berapapun','berarti','berawal','berbagai','berdatangan','beri','berikan',
        'berikut','berikutnya','berjumlah','berkali-kali','berkata','berkehendak','berkeinginan',
        'berkenaan','berlainan','berlalu','berlangsung','berlebihan','bermacam','bermacam-macam',
        'bermaksud','bermula','bersama','bersama-sama','bersiap','bersiap-siap','bertanya',
        'bertanya-tanya','berturut','berturut-turut','bertutur','berujar','berupa','besar',
        'betul','betulkah','bgt','biar','biasa','biasanya','bila','bilakah','bisa','bisakah','blm','blom','boleh',
        'bolehkah','bolehlah','br','bu','buat','bukan','bukankah','bukanlah','bukannya','bulan','bung','c','cara',
        'caranya','cukup','cukupkah','cukuplah','cuma','cuman','d','dah','dahulu','dalam','dan','dapat','dapet','dari',
        'daripada','datang','deh','dekat','demi','demikian','demikianlah','dengan','depan','di','dia',
        'diakhiri','diakhirinya','dialah','diantara','diantaranya','diberi','diberikan','diberikannya',
        'dibuat','dibuatnya','didapat','didatangkan','digunakan','diibaratkan','diibaratkannya',
        'diingat','diingatkan','diinginkan','dijawab','dijelaskan','dijelaskannya','dikarenakan',
        'dikatakan','dikatakannya','dikerjakan','diketahui','diketahuinya','dikira','dilakukan',
        'dilalui','dilihat','dimaksud','dimaksudkan','dimaksudkannya','dimaksudnya','dimana','diminta',
        'dimintai','dimisalkan','dimulai','dimulailah','dimulainya','dimungkinkan','dini','dipastikan',
        'diperbuat','diperbuatnya','dipergunakan','diperkirakan','diperlihatkan','diperlukan',
        'diperlukannya','dipersoalkan','dipertanyakan','dipunyai','diri','dirinya','disampaikan',
        'disebut','disebutkan','disebutkannya','disini','disinilah','ditambahkan','ditandaskan',
        'ditanya','ditanyai','ditanyakan','ditegaskan','ditujukan','ditunjuk','ditunjuki','ditunjukkan',
        'ditunjukkannya','ditunjuknya','dituturkan','dituturkannya','diucapkan','diucapkannya',
        'diungkapkan','doang','dong','donk','dpt','dr','dua','dulu','dy','e','eh','elu','emang','empat','emg','enak',
        'engga','enggak','enggaknya','entah','entahlah','entar','f','g','ga','gak','gapapa','gih','gimana','gini','gitu',
        'gk','gmn','gua','gue','guna','gunakan','gw','h','hadap','hah','haha','hahaha','hahahaha','hai','hal','halo','hallo',
        'hampir','hanya','hanyalah','hari','harus','haruslah','harusnya','hehe','hehehe','helo','hello','hendak','hendaklah',
        'hendaknya','hingga','i','ia','ialah','ibarat','ibaratkan','ibaratnya','ibu','ikut','ingat','ingat-ingat','ingin',
        'inginkah','inginkan','ini','inikah','inilah','itu','itukah','itulah','iy','iya','iyaa','j','jadi','jadilah',
        'jadinya','jangan','jangankan','janganlah','jauh','jawab','jawaban','jawabnya','jd','jg','jgn','jelas',
        'jelaskan','jelaslah','jelasnya','jika','jikalau','juga','jumlah','jumlahnya','justru',
        'k','kadar','kagak','kala','kalau','kalaulah','kalaupun','kali','kalian','kalo','kami','kamilah','kamu',
        'kamulah','kan','kapan','kapankah','kapanpun','karena','karenanya','karna','kasus','kata','katakan',
        'katakanlah','katanya','kayak', 'kayaknya','kayanya','ke','keadaan','kebetulan','kecil','kedua','keduanya','keinginan',
        'kelamaan','kelihatan','kelihatannya','kelima','keluar','kembali','kemudian','kemungkinan',
        'kemungkinannya','kena','kenapa','kepada','kepadanya','kerja','kesampaian','keseluruhan',
        'keseluruhannya','keterlaluan','ketika','khusus','khususnya','kini','kinilah','kira',
        'kira-kira','kiranya','kita','kitalah','kl','klo','km','kok','kurang','kyk','kyknya','kynya','l','lagi','lagian',
        'lah','lain','lainnya','laku','lalu','lama','lamanya','langsung','lanjut','lanjutnya','lebih','lewat','lg',
        'lihat','lima','lu','luar','lo','lw','m','macam','mah','maka','makanya','makin','maksud','malah','malahan',
        'mampu','mampukah','mana','manakala','manalagi','masa','masalah','masalahnya','masih',
        'masihkah','masing','masing-masing','masuk','mata','mau','maupun','melainkan','melakukan',
        'melalui','melihat','melihatnya','memang','memastikan','memberi','memberikan','membuat',
        'memerlukan','memihak','meminta','memintakan','memisalkan','memperbuat','mempergunakan',
        'memperkirakan','memperlihatkan','mempersiapkan','mempersoalkan','mempertanyakan','mempunyai',
        'memulai','memungkinkan','menaiki','menambahkan','menandaskan','menanti','menanti-nanti',
        'menantikan','menanya','menanyai','menanyakan','mendapat','mendapatkan','mendatang','mendatangi',
        'mendatangkan','menegaskan','mengakhiri','mengapa','mengatakan','mengatakannya','mengenai',
        'mengerjakan','mengetahui','menggunakan','menghendaki','mengibaratkan','mengibaratkannya',
        'mengingat','mengingatkan','menginginkan','mengira','mengucapkan','mengucapkannya','mengungkapkan',
        'menjadi','menjawab','menjelaskan','menuju','menunjuk','menunjuki','menunjukkan','menunjuknya',
        'menurut','menuturkan','menyampaikan','menyangkut','menyatakan','menyebutkan','menyeluruh',
        'menyiapkan','merasa','mereka','merekalah','merupakan','meski','meskipun','meyakini','meyakinkan',
        'minta','mirip','misal','misalkan','misalnya','mohon','msh','mula','mulai','mulailah','mulanya','mungkin',
        'mungkinkah','n','nah','naik','namun','nanti','nantinya','ngak','ngga','nggak','ni','nih','nnt','no','ntar','ntr',
        'nya','nyaris','nyata','nyatanya','o','oh','ok','oke','oleh','olehnya','orang','p','pa','pada','padahal','padanya','pak',
        'paling','panjang','pantas','para','pas','pasti','pastilah','penting','pentingnya','per','percuma','perlu','perlukah',
        'perlunya','pernah','persoalan','pertama','pertama-tama','pertanyaan','pertanyakan','pihak','pihaknya',
        'pukul','pula','pun','punya','q','r','rasa','rasanya','rupa','rupanya','s','saat','saatnya','saja',
        'sajalah','salam','saling','sama','sama-sama','sambil','sampai','sampai-sampai','sampaikan','sana',
        'sangat','sangatlah','sangkut','satu','saya','sayalah','se','sdh','sebab','sebabnya','sebagai',
        'sebagaimana','sebagainya','sebagian','sebaik','sebaik-baiknya','sebaiknya','sebaliknya',
        'sebanyak','sebegini','sebegitu','sebelum','sebelumnya','sebenarnya','seberapa','sebesar',
        'sebetulnya','sebisanya','sebuah','sebut','sebutlah','sebutnya','secara','secukupnya','sedang',
        'sedangkan','sedemikian','sedikit','sedikitnya','seenaknya','segala','segalanya','segera',
        'seharusnya','sehingga','seingat','sejak','sejauh','sejenak','sejumlah','sekadar','sekadarnya',
        'sekali','sekali-kali','sekalian','sekaligus','sekalipun','sekarang','sekaranglah','sekecil',
        'seketika','sekiranya','sekitar','sekitarnya','sekurang-kurangnya','sekurangnya','sela','selain',
        'selaku','selalu','selama','selama-lamanya','selamanya','selanjutnya','seluruh','seluruhnya',
        'semacam','semakin','semampu','semampunya','semasa','semasih','semata','semata-mata','semaunya',
        'sementara','semisal','semisalnya','sempat','semua','semuanya','semula','sendiri','sendirian',
        'sendirinya','seolah','seolah-olah','seorang','sepanjang','sepantasnya','sepantasnyalah',
        'seperlunya','seperti','sepertinya','sepihak','sering','seringnya','serta','serupa','sesaat',
        'sesama','sesampai','sesegera','sesekali','seseorang','sesuatu','sesuatunya','sesudah',
        'sesudahnya','setelah','setempat','setengah','seterusnya','setiap','setiba','setibanya',
        'setidak-tidaknya','setidaknya','setinggi','seusai','sewaktu','si','siap','siapa','siapakah',
        'siapapun','sih','sini','sinilah','sm','soal','soalnya','suatu','sudah','sudahkah','sudahlah','supaya',
        't','tadi','tadinya','tahu','tau','tak','tambah','tambahnya','tampak','tampaknya','tandas','tandasnya',
        'tanpa','tanya','tanyakan','tanyanya','tapi','td','tegas','tegasnya','telah','tempat','tentang','tentu',
        'tentulah','tentunya','tepat','terakhir','terasa','terbanyak','terdahulu','terdapat','terdiri',
        'terhadap','terhadapnya','teringat','teringat-ingat','terjadi','terjadilah','terjadinya','terkira',
        'terlalu','terlebih','terlihat','termasuk','ternyata','tersampaikan','tersebut','tersebutlah',
        'tertentu','tertuju','terus','terutama','tetap','tetapi','tetep','tiap','tiba','tiba-tiba','tidak',
        'tidakkah','tidaklah','tiga','toh','tp','trus','ttp','tuh','tuju','tunjuk','turut','tutur','tuturnya','u',
        'ucap','ucapnya','ud','udah','udh','ujar','ujarnya','umumnya','ungkap','ungkapnya','untuk','usah','usai','utk',
        'v','w','waduh','wah','wahai','waktunya','walau','walaupun','wk','wkwk','wkwkwk','wkwkwkwk','wong','x','y','ya',
        'yaa','yah','yaitu','yak','yakin','yakni','yang','yg','z'}
}