<?php
// Bot tokeningiz
define('API_TOKEN', '8988913587:AAFnXQYlUAgGJe_qZWFTMK1c16y6sR65-Kg');

// Web App manzili (HTTPS bo'lishi shart!)
define('WEB_APP_URL', 'https://sizning-saytingiz.com/index.html'); // O'z saytingiz manzili bilan almashtiring!

$update = json_decode(file_get_contents('php://input'), true);
$chat_id = $update['message']['chat']['id'] ?? $update['callback_query']['message']['chat']['id'] ?? null;
$text = $update['message']['text'] ?? null;

if (!$chat_id) exit;

function sendMessage($chat_id, $text, $keyboard = null) {
    $url = "https://api.telegram.org/bot" . API_TOKEN . "/sendMessage";
    $post_fields = [
        'chat_id' => $chat_id,
        'text' => $text,
        'reply_markup' => json_encode($keyboard),
        'parse_mode' => 'HTML'
    ];
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post_fields);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_exec($ch);
    curl_close($ch);
}

// Asosiy menyu
$menu = [
    'keyboard' => [
        [['text' => 'BRON QILISH', 'web_app' => ['url' => WEB_APP_URL]]],
        [['text' => 'ADMIN BILAN BOGLANISH']],
        [['text' => 'GAME CLUB JOYLASHUVI']]
    ],
    'resize_keyboard' => true
];

// Buyruqlarni ishlash
if ($text == '/start') {
    sendMessage($chat_id, "Keldi Botga xush kelibsiz! Quyidagilardan birini tanlang:", $menu);
} elseif ($text == 'ADMIN BILAN BOGLANISH') {
    sendMessage($chat_id, "👤 Admin: Zuxriddinov Boxoviddin\n📞 Telefon: +998886577553\nSavollaringiz bo'lsa, bog'lanishingiz mumkin.");
} elseif ($text == 'GAME CLUB JOYLASHUVI') {
    $info = "Xush kelibsiz! Bizning Game Club — bu sizning eng yaxshi hordiq maskaningiz! \n\n" .
            "Bizda eng so'nggi rusumdagi kuchli kompyuterlar va ultra tezkor internet mavjud. \n" .
            "Qulay kreslolar va yumshoq muhit sizga haqiqiy geymerlik zavqini taqdim etadi. \n" .
            "Do'stlaringiz bilan birga o'yin o'ynash uchun eng ideal joy. \n" .
            "Sifatli servis va doimo yordamga tayyor operatorlarimiz sizni kutmoqda. \n" .
            "Biz har kuni 24/7 sizning xizmatingizdamiz. \n" .
            "Joylashuvimiz juda qulay: Andijon viloyati, Shahrixon tumani. \n" .
            "Tojmahal to'yxonasi yonida joylashganmiz, kirib kelishingizni kutamiz! \n" .
            "Shunchaki o'yin emas, balki sifatli dam olishni tanlang. \n" .
            "Biz bilan o'yindan olingan zavq yanada yuqori darajada bo'ladi!";
    sendMessage($chat_id, $info);
}
?>
