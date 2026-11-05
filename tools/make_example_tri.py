#!/usr/bin/env python3
"""Tao weeks-tri/example-week.json: tuan 1 cua Tri o dang RUT GON (de xem dinh dang va thu web), khong phai tuan day du."""
import json, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "weeks-tri", "example-week.json")

def S(type_, items, ins="", core=None, **kw):
    d = {"type": type_}
    if ins: d["instruction"] = ins
    d["core"] = core or len(items); d["items"] = items; d.update(kw); return d
def mcq(q, o, a, why): return {"q": q, "options": o, "answer": a, "why": why}

VL = [
 ("job displacement","tình trạng mất việc do bị thay thế","noun phrase","/dʒɒb dɪsˈpleɪsmənt/","Rapid job displacement has left many mid-career workers struggling to adapt.",1),
 ("labour market","thị trường lao động","noun phrase","/ˈleɪbə ˈmɑːkɪt/","The labour market now rewards flexibility above loyalty.",1),
 ("skills gap","khoảng cách kỹ năng","noun phrase","/skɪlz ɡæp/","A widening skills gap leaves vacancies unfilled in every sector.",1),
 ("redundancy","tình trạng bị sa thải do dư thừa","noun","/rɪˈdʌndənsi/","Redundancy rarely comes with a plan for retraining.",1),
 ("gig economy","nền kinh tế làm việc tự do ngắn hạn","noun phrase","/ɡɪɡ ɪˈkɒnəmi/","The gig economy offers flexibility but little protection.",1),
 ("workforce","lực lượng lao động","noun","/ˈwɜːkfɔːs/","An ageing workforce must be retrained, not replaced.",1),
 ("be made redundant","bị cho thôi việc","phrase","/biː meɪd rɪˈdʌndənt/","Thousands are likely to be made redundant once the factory is automated.",1),
 ("boost productivity","tăng năng suất","verb phrase","/buːst ˌprɒdʌkˈtɪvəti/","Robots can boost productivity without raising wages.",2),
 ("cut costs","cắt giảm chi phí","verb phrase","/kʌt kɒsts/","Firms automate mainly to cut costs.",2),
 ("streamline operations","tinh gọn hoạt động","verb phrase","/ˈstriːmlaɪn ˌɒpəˈreɪʃnz/","Software helps companies streamline operations across borders.",2),
 ("a double-edged sword","con dao hai lưỡi","idiom","/ə ˌdʌbl ˈedʒd sɔːd/","Automation is a double-edged sword for low-skilled workers.",2),
 ("reap the benefits","gặt hái lợi ích","idiom","/riːp ðə ˈbenɪfɪts/","Early adopters reap the benefits of new technology.",2),
 ("cutting-edge","tiên tiến nhất","adjective","/ˌkʌtɪŋ ˈedʒ/","Cutting-edge machinery now performs tasks once done by hand.",2),
 ("labour-saving","tiết kiệm sức lao động","adjective","/ˈleɪbə ˌseɪvɪŋ/","Labour-saving devices free staff for more creative work.",2),
 ("widen the inequality gap","nới rộng khoảng cách bất bình đẳng","verb phrase","/ˈwaɪdn ði ˌɪnɪˈkwɒləti ɡæp/","Unchecked automation could widen the inequality gap.",3),
 ("job security","sự ổn định việc làm","noun phrase","/dʒɒb sɪˈkjʊərəti/","Job security can no longer be taken for granted.",3),
 ("erode skills","làm mai một kỹ năng","verb phrase","/ɪˈrəʊd skɪlz/","Overreliance on software may erode skills that took years to build.",3),
 ("put people out of work","khiến người ta mất việc","verb phrase","/pʊt ˈpiːpl aʊt əv wɜːk/","New machines can put people out of work overnight.",3),
 ("a growing sense of insecurity","cảm giác bất an ngày một tăng","noun phrase","/ə ˈɡrəʊɪŋ sens əv ˌɪnsɪˈkjʊərəti/","A growing sense of insecurity is spreading through white-collar jobs.",3),
 ("overreliance on","sự phụ thuộc quá mức vào","noun phrase","/ˌəʊvəriˈlaɪəns ɒn/","Overreliance on algorithms weakens human judgement.",3),
 ("fall short of","không đạt được","phrasal verb","/fɔːl ʃɔːt əv/","Government support often falls short of what retrained workers need.",3),
 ("reskill","đào tạo lại kỹ năng","verb","/ˌriːˈskɪl/","Workers must reskill every few years to stay employable.",4),
 ("lifelong learning","học tập suốt đời","noun phrase","/ˌlaɪflɒŋ ˈlɜːnɪŋ/","Lifelong learning is now a survival skill.",4),
 ("adapt to","thích nghi với","phrasal verb","/əˈdæpt tuː/","Societies must adapt to change faster than before.",4),
 ("strike a balance","tìm được sự cân bằng","idiom","/straɪk ə ˈbæləns/","Policy should strike a balance between innovation and fairness.",4),
 ("safety net","mạng lưới an sinh","noun phrase","/ˈseɪfti net/","A strong safety net makes change less frightening.",4),
 ("a pressing issue","một vấn đề cấp bách","noun phrase","/ə ˈpresɪŋ ˈɪʃuː/","Retraining is a pressing issue for every government.",4),
 ("mitigate the impact","giảm nhẹ tác động","verb phrase","/ˈmɪtɪɡeɪt ði ˈɪmpækt/","Early support can mitigate the impact on displaced workers.",4),
]
vocabList = [{"en":a,"vi":b,"pos":c,"ipa":d,"ex":e,"sub":f} for a,b,c,d,e,f in VL]
def vmap(sub): return {x["en"]: x["vi"] for x in vocabList if x["sub"] == sub}

T1 = "Few debates are as heated as the one about job displacement. Across the labour market, a widening skills gap leaves employers short of talent, while thousands face redundancy. The rise of the gig economy has reshaped the workforce, offering flexibility but little protection. Not every worker is lucky: many risk having to be made redundant when their tasks are automated. Rarely has the labour market changed so quickly."
T2 = "Supporters argue that robots boost productivity and cut costs. Firms that streamline operations with cutting-edge systems reap the benefits quickly, and labour-saving machines free staff from dull tasks. Yet automation remains a double-edged sword. Not only does it raise output, but it also changes who is needed."
T3 = "Critics warn that automation will widen the inequality gap. Job security, once taken for granted, is fading, and a growing sense of insecurity affects even skilled staff. Overreliance on machines can erode skills, and software that can put people out of work will not easily create new jobs. Never before have policies so often fall short of the pace of change."
T4 = "The way forward is to reskill workers. Lifelong learning helps people adapt to new roles, and governments must strike a balance between innovation and a safety net. This is a pressing issue, and we must mitigate the impact on those most affected."
T7 = "The debate about automation is often reduced to slogans. In truth, job displacement is only one part of a wider story. In the labour market, a persistent skills gap coexists with redundancy, and the workforce is increasingly shaped by the gig economy; those who fail to adapt may be made redundant. On the positive side, firms claim that new tools boost productivity, cut costs and streamline operations. Cutting-edge, labour-saving technology lets them reap the benefits, yet it remains a double-edged sword. Critics counter that it will widen the inequality gap, weaken job security and create a growing sense of insecurity. Overreliance on algorithms can erode skills, and systems that put people out of work may fall short of what society expects. The answer is neither panic nor complacency. Governments should help people reskill, support lifelong learning, and adapt to change. They must strike a balance between growth and fairness, build a safety net, and treat this as a pressing issue so as to mitigate the impact. Seldom has the choice mattered so much."

def tx(t): return [t]
def read(key, title, heading, purpose, text, sub, comp, apply, mins="5–17′", note=None, preview=False):
    d = {"type":"read","key":key,"title":title,"min":mins,"heading":heading,"purpose":purpose,"text":tx(text),"vocab":vmap(sub) if sub else {},"sets":[comp, apply]}
    if note: d["note"] = note
    return d
def notice():
    return {"type":"notice","key":"notice","title":"Tìm ngữ pháp","min":"24–30′","text":tx(T1),"target":["rarely","not every"],"find":"cấu trúc đảo ngữ và câu phủ định mở đầu câu",
      "box":{"title":"Ghi nhớ: đảo ngữ sau trạng từ phủ định","intro":"Sau Not only, Rarely, Never, Seldom, Hardly... đặt trợ động từ trước chủ ngữ.",
        "rows":[{"subject":"Not only + trợ động từ + S + V","form":"Not only does it raise output, but ...","example":"Not only does it raise output, but it also changes who is needed."},
                {"subject":"Rarely / Seldom / Never + trợ động từ + S","form":"Rarely has the labour market changed so quickly.","example":"Never before have policies so often fallen short."}],
        "note":"Lỗi thường gặp: quên đảo (Rarely the market has...) hoặc đảo cả ở mệnh đề sau but also."}}

Q1 = S("mcq",[mcq("Which sentence is correct?",["Rarely has the labour market changed so quickly.","Rarely the labour market has changed so quickly.","Rarely the labour market changed has so quickly."],"Rarely has the labour market changed so quickly.","Sau Rarely, trợ động từ has đứng trước chủ ngữ."),
  mcq("The author's attitude to automation is best described as","balanced but cautious,enthusiastic,dismissive".split(","),"balanced but cautious","Tác giả nêu cả lợi ích lẫn rủi ro và kêu gọi cân bằng."),
  mcq("Which pair best fits the gap: ___ displacement and the skills ___?",["job / gap","work / hole","job / hole"],"job / gap","Collocation cố định: job displacement, skills gap.")],"Chọn đáp án đúng nhất theo bài đọc.")
APPLY1 = S("answer",[{"prompt":"Rewrite with Rarely: \"The labour market has seldom changed so quickly.\"","answer":"Rarely has the labour market changed so quickly.","why":"Đảo has trước chủ ngữ."},
  {"prompt":"In one sentence, say how the gig economy affects workers, using \"but\".","answer":"The gig economy offers flexibility but little protection.","alt":[]}],"Dùng cấu trúc và cụm của bài để trả lời.",role="apply")

def warm(items, ungraded=False): d = S("mcq", items, "Chọn đáp án đúng nhất."); d["core"]=len(items); d.update({"ungraded":True} if ungraded else {}); return d

def out_write(prompt, hint, sample, model, minw, use, outline=None, data=None, check=None, mins="48–60′"):
    d = {"type":"output","key":"output","title":"Tự viết","min":mins,"prompt":prompt,"hint":hint,"sample":sample,"model":model,"minWords":minw,"useWords":use}
    if outline: d["outline"] = outline
    if data: d["data"] = data
    if check: d["checklist"] = check
    return d
def out_speak(prompt, sample, model, sec, mins="48–60′"):
    return {"type":"output","key":"output","title":"Tự nói","min":mins,"mode":"speak","seconds":sec,"prompt":prompt,"hint":"Start with your position.","sample":sample,"model":model}

listen = lambda text, items: {"type":"listen","key":"listen","title":"Nghe","min":"17–24′","text":tx(text),"sets":[S("listenpick",items,"Nghe rồi chọn đáp án đúng.")]}
LP = lambda say,q,o,a,why: {"say":say,"q":q,"options":o,"answer":a,"why":why}

mon = {"title":"Sub 1: The changing job market","kind":"new","steps":[
  {"type":"sets","key":"warmup","title":"Khởi động","min":"0–5′","sets":[warm([mcq("\"Job displacement\" most likely means",["losing jobs to new technology","moving to a new job","changing office"],"losing jobs to new technology","displacement = bị thay thế."),mcq("\"A skills gap\" is",["a shortage of the right skills","a long holiday","a pay rise"],"a shortage of the right skills","gap = khoảng cách.")],True)]},
  read("read","Đọc","Is automation a threat or an opportunity?","Đọc để tìm: tác giả mô tả thị trường lao động thay đổi thế nào?",T1,1,Q1,APPLY1),
  listen(T1,[LP("Rarely has the labour market changed so quickly.","Điều gì hiếm khi xảy ra?",["Thị trường lao động thay đổi nhanh đến vậy","Việc làm tăng","Lương giảm"],"Thị trường lao động thay đổi nhanh đến vậy","Rarely + has + chủ ngữ."),LP("The gig economy offers flexibility but little protection.","Gig economy thiếu điều gì?",["Sự bảo vệ","Sự linh hoạt","Thu nhập"],"Sự bảo vệ","little protection.")]),
  notice(),
  {"type":"sets","key":"practice","title":"Luyện tập","min":"30–48′","sets":[
    S("form",[{"text":"The ___ (ADEQUATE) of the existing safety net became clear during the crisis.","answer":"inadequacy","why":"Cần danh từ phủ định: inadequacy."},{"text":"A ___ (GROW) sense of insecurity is spreading.","answer":"growing","why":"Cần tính từ V-ing đứng trước danh từ."}],"Điền dạng đúng của từ trong ngoặc."),
    S("cloze",[{"answer":"has","why":"Đảo has sau Rarely."},{"answer":"does","why":"Đảo does sau Not only."}],"Gõ từ còn thiếu vào đoạn văn.",passage="Rarely ___ the workforce faced such change. Not only ___ automation cut costs, but it also raises quality.",mode="type"),
    S("transform",[{"prompt":"Automation cuts costs and it also raises quality.","instruction":"Viết lại bằng Not only ... but also, dùng từ gợi ý.","keyword":"does","answer":"Not only does automation cut costs, but it also raises quality.","alt":["Not only does automation cut costs but it also raises quality."],"why":"Not only đứng đầu thì đảo does automation."}],"Viết lại câu theo yêu cầu.")]},
  out_write("Write one paragraph (70 to 100 words) stating your position on whether automation helps or harms workers.","Open with a clear thesis.","Rarely has a technology divided workers so sharply. In my view, automation is a double-edged sword.","Never before has the labour market changed so rapidly, yet the answer is not to resist change but to prepare for it. Not only does automation cut costs, but it also frees people from repetitive work.",60,["Rarely","Not only","Never"],["Câu chủ đề nêu luận điểm","Lý do và bằng chứng","Kết nối với tuần sau"],check=["Có luận điểm rõ ở câu đầu","Dùng ít nhất một cấu trúc đảo ngữ đúng","Có lý do hoặc ví dụ cụ thể"],mins="48–60′")]}

tue = {"title":"Ôn Sub 1, đọc trước Sub 2","kind":"review","steps":[
  {"type":"sets","key":"warmup","title":"Nhớ lại","min":"0–5′","sets":[warm([mcq("Which sentence needs inversion?",["Rarely ... the market has changed.","The market has changed quickly.","Many workers adapt."],"Rarely ... the market has changed.","Rarely mở đầu câu thì đảo.")])]},
  {"type":"sets","key":"review","title":"Ôn dạng bài khác","min":"5–36′","sets":[
    S("fix",[{"wrong":"Never before the labour market has changed so quickly.","answer":"Never before has the labour market changed so quickly.","why":"Sau Never before phải đảo: has + chủ ngữ."},{"wrong":"Not only automation cuts costs, but it also raises quality.","answer":"Not only does automation cut costs, but it also raises quality.","why":"Thiếu trợ động từ does sau Not only."}],"Tìm và sửa lỗi."),
    S("gap",[{"text":"A widening skills ___ leaves vacancies unfilled.","answer":"gap","why":"skills gap."},{"text":"Many workers risk being made ___.","answer":"redundant","why":"be made redundant."}],"Điền từ vào chỗ trống."),
    S("reorder",[{"words":["Rarely","have","economists","agreed","on","such","a","complex","issue"],"answer":"Rarely have economists agreed on such a complex issue.","why":"Rarely + have + chủ ngữ."}],"Xếp thành câu hoàn chỉnh.")]},
  read("preview","Đọc trước Sub 2","The case for automation","Đọc để tìm: hai lợi ích chính mà người ủng hộ nêu ra.",T2,2,S("answer",[{"prompt":"Which two benefits do supporters mention?","answer":"Higher productivity and lower costs.","alt":[]}],"Trả lời ngắn.",role="apply"),S("answer",[{"prompt":"What do you think a double-edged sword means here?","answer":"Something with both benefits and harms.","alt":[]}],"Đoán nghĩa theo ngữ cảnh.",role="apply"),mins="36–46′",note="Hôm nay chỉ đọc để làm quen; đầy đủ vào Thứ 4."),
  out_write("The paragraph below is weak. Rewrite it (60 to 80 words) using at least two inversion structures: \"Automation is changing jobs. It makes firms cheaper. It also makes work faster. Workers are worried about it.\"","Start with Rarely or Not only.","Not only does automation make firms cheaper, but it also makes work faster.","Rarely have workers faced such a mix of promise and threat. Not only does automation cut costs, but it also speeds up work; nevertheless, many people worry about losing their jobs.",50,["Not only","Rarely"],mins="46–60′")]}

wed = {"title":"Sub 2: The case for automation","kind":"new","steps":[
  {"type":"sets","key":"warmup","title":"Nhớ lại","min":"0–5′","sets":[warm([mcq("Complete: Not only ___ it cut costs, but it also boosts quality.",["does","do","is"],"does","Đảo does trước it.")])]},
  read("read","Đọc","The case for automation","Đọc để tìm: vì sao tự động hóa được gọi là con dao hai lưỡi?",T2,2,S("mcq",[mcq("According to the text, firms that streamline operations",["reap the benefits quickly","lose staff","raise prices"],"reap the benefits quickly","Câu 2 của đoạn.")],"Chọn đáp án đúng."),S("transform",[{"prompt":"Robots boost productivity and cut costs.","instruction":"Viết lại với Not only ... but also.","answer":"Not only do robots boost productivity, but they also cut costs.","alt":["Not only do robots boost productivity but they also cut costs."],"why":"Đảo do trước robots."}],"Dùng cấu trúc của tuần.",role="apply"),mins="5–17′"),
  listen(T2,[LP("Not only does it raise output, but it also changes who is needed.","Ý nào đúng?",["Tự động hóa tăng sản lượng và thay đổi nhu cầu nhân lực","Chỉ tăng sản lượng","Chỉ giảm nhân lực"],"Tự động hóa tăng sản lượng và thay đổi nhu cầu nhân lực","Hai vế của Not only ... but also.")]),
  {"type":"sets","key":"practice","title":"Luyện tập","min":"30–48′","sets":[S("mcq",[mcq("___ has so much changed in so short a time.",["Seldom","Not only","Such"],"Seldom","Seldom + has đảo.")],"Chọn từ đúng."),S("fix",[{"wrong":"Hardly the workers had arrived when the machines started.","answer":"Hardly had the workers arrived when the machines started.","why":"Hardly + had + chủ ngữ."}],"Sửa lỗi.")]},
  out_write("Write an argument (130 to 170 words): should firms automate as fast as possible? Include one counter-argument and a rebuttal.","Claim, reason, evidence, counter-argument, rebuttal.","Firms should not automate blindly. Rarely do quick fixes serve everyone.","Not only can automation cut costs, but it can also protect workers from dangerous tasks. Critics may argue that it destroys jobs; however, history shows that new roles emerge, so the real task is retraining.",110,["Not only","Rarely","a double-edged sword"],["Claim","Reason + evidence","Counter-argument","Rebuttal"],mins="48–60′")]}

thu = {"title":"Ôn Sub 1–2, đọc trước Sub 3","kind":"review","steps":[
  {"type":"sets","key":"warmup","title":"Nhớ lại","min":"0–5′","sets":[warm([mcq("\"Cutting-edge\" means",["most advanced","very old","cheap"],"most advanced","cutting-edge = tiên tiến nhất.")])]},
  {"type":"sets","key":"review","title":"Ôn dạng bài khác","min":"5–36′","sets":[S("cloze",[{"answer":"has","why":"Đảo has sau Never before."},{"answer":"does","why":"Đảo does sau Not only."}],"Gõ từ còn thiếu.",passage="Never before ___ the workforce been so mobile. Not only ___ it want flexibility, but it also demands security.",mode="type"),S("dictation",[{"say":"Not only does automation boost productivity, but it also frees workers from repetitive tasks.","why":"Chú ý đảo does automation."}],"Nghe và gõ lại câu.")]},
  read("preview","Đọc trước Sub 3","The risks","Đọc để tìm: ba rủi ro mà các nhà phê bình nêu.",T3,3,S("answer",[{"prompt":"Name one risk mentioned.","answer":"A growing sense of insecurity.","alt":["Job security is fading."]}],"Trả lời ngắn.",role="apply"),S("answer",[{"prompt":"What does overreliance on machines do?","answer":"It can erode skills.","alt":[]}],"Trả lời ngắn.",role="apply"),mins="36–46′",note="Hôm nay chỉ đọc để làm quen."),
  out_speak("Speak for 60 seconds: rebut the claim that automation always destroys jobs.","Let me be clear: automation does not always destroy jobs.","Let me be clear from the outset: automation does not always destroy jobs. Consider this: rarely has technology reduced total employment in the long run. New roles emerge, and the real challenge is retraining.",60,mins="46–60′")]}

fri = {"title":"Sub 3: The risks","kind":"new","steps":[
  {"type":"sets","key":"warmup","title":"Nhớ lại","min":"0–5′","sets":[warm([mcq("\"Erode skills\" means to",["weaken skills gradually","teach skills","test skills"],"weaken skills gradually","erode = bào mòn.")])]},
  read("read","Đọc","The risks","Đọc để tìm: vì sao người lao động có cảm giác bất an?",T3,3,S("mcq",[mcq("The text suggests policies",["fall short of the pace of change","are too fast","are unnecessary"],"fall short of the pace of change","Câu cuối đoạn.")],"Chọn đáp án đúng."),S("transform",[{"prompt":"Policies have never before fallen so far short.","instruction":"Viết lại bắt đầu bằng Never before.","answer":"Never before have policies fallen so far short.","alt":[],"why":"Never before + have + chủ ngữ."}],"Dùng cấu trúc của tuần.",role="apply"),mins="5–17′"),
  listen(T3,[LP("Overreliance on machines can erode skills.","Overreliance gây hại gì?",["Làm mai một kỹ năng","Tăng lương","Giảm giờ làm"],"Làm mai một kỹ năng","erode skills.")]),
  {"type":"sets","key":"practice","title":"Luyện tập","min":"30–48′","sets":[S("dialogue",[{"lines":["Automation will inevitably destroy more jobs than it creates."],"options":["That may hold in the short term, but history suggests new sectors absorb displaced workers.","I do not agree.","Jobs are good."],"answer":"That may hold in the short term, but history suggests new sectors absorb displaced workers.","why":"Nhượng bộ một phần rồi phản biện bằng bằng chứng."}],"Chọn câu đáp thuyết phục nhất."),S("translate",[{"prompt":"Hiếm khi nào các chính phủ phải đối mặt với một thay đổi nhanh đến vậy.","answer":"Rarely have governments faced such rapid change.","why":"Rarely mở đầu nên đảo have governments."}],"Dịch sang tiếng Anh (tự chấm).")]},
  out_speak("Speak for 90 seconds: persuade your audience that governments must act on job insecurity.","Let me be blunt: job insecurity is a policy failure.","Let me be blunt: job insecurity is a policy failure. Rarely have workers had so little protection, and never before has the pace of change been so fast. We must act now.",90,mins="48–60′")]}

sat = {"title":"Ôn cả tuần, giới thiệu Sub 4","kind":"week","steps":[
  {"type":"sets","key":"quiz","title":"Quiz tuần","min":"0–6′","sets":[S("mcq",[mcq("Which is correct?",["Seldom have workers felt so secure.","Seldom workers have felt so secure.","Seldom felt workers have so secure."],"Seldom have workers felt so secure.","Seldom + have + chủ ngữ.")],"Chọn đáp án đúng.")]},
  read("transfer","Đọc mới","Automation: a balanced view","Đọc để tìm: tác giả đề xuất giải pháp nào?",T7,None,S("mcq",[mcq("The author's main recommendation is to",["help people reskill and build a safety net","ban automation","ignore the issue"],"help people reskill and build a safety net","Câu gần cuối.")],"Chọn đáp án đúng."),S("answer",[{"prompt":"Why does the author call automation a double-edged sword?","answer":"It brings benefits but also risks.","alt":[]}],"Trả lời ngắn.",role="apply"),mins="6–20′"),
  {"type":"sets","key":"mix","title":"Tổng hợp","min":"20–38′","sets":[S("fix",[{"wrong":"Rarely workers have faced such pressure.","answer":"Rarely have workers faced such pressure.","why":"Đảo have workers."}],"Tìm và sửa lỗi."),S("dictation",[{"say":"Never before have policies so often fallen short of the pace of change.","why":"Never before + have + chủ ngữ."}],"Nghe và gõ lại.")]},
  read("preview","Đọc trước Sub 4","The way forward","Đọc để tìm: hai biện pháp được đề xuất.",T4,4,S("answer",[{"prompt":"Name one measure proposed.","answer":"Lifelong learning.","alt":["A safety net."]}],"Trả lời ngắn.",role="apply"),S("answer",[{"prompt":"What must governments balance?","answer":"Innovation and fairness.","alt":[]}],"Trả lời ngắn.",role="apply"),mins="38–44′",note="Hôm nay chỉ đọc để làm quen."),
  out_write("DATA REPORT (format demo). The line graph shows the share of tasks automated in two sectors. Summarise the information (at least 150 words).","The graph illustrates ... Overall, ...","The line graph illustrates the proportion of tasks automated in manufacturing and services between 2000 and 2030.","Overall, both sectors show a steep upward trend, with manufacturing consistently ahead. Manufacturing rose from 12% in 2000 to 55% in 2020 and is projected to reach 78% by 2030, whereas services climbed from just 5% to 32% over the same period.",150,["Overall","whereas","is projected to","a sharp rise in"],["Paraphrase","Overview","Detail 1","Detail 2"],data={"title":"Share of tasks automated, by sector","unit":"%","kind":"line","headers":["Year","Manufacturing","Services"],"rows":[["2000",12,5],["2010",30,14],["2020",55,32],["2030",78,60]],"note":"Fictional data for practice. The 2030 figures are projections."},mins="44–56′"),
  {"type":"report","key":"report","title":"Báo cáo tuần","min":"56–60′"}]}

week = {"schema":"a1-week/1","week":1,"title":"Work and automation","grammar":"Đảo ngữ sau trạng từ phủ định (Not only, Rarely, Never)","level":"B2-C1","focus":"Viết đoạn luận điểm và bài nói mở đầu thuyết phục",
  "subs":["The changing job market","The case for automation","The risks","The way forward"],"vocabList":vocabList,
  "sessions":{"mon":mon,"tue":tue,"wed":wed,"thu":thu,"fri":fri,"sat":sat},"challenges":{}}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(week, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(os.path.join(os.path.dirname(OUT), "index.json"), "w").write("[]\n")
print("ok", os.path.getsize(OUT))
