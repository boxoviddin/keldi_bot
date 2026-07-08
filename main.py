<?php
// Bot tokeningiz va Admin ID
define('API_TOKEN', '8988913587:AAFnXQYlUAgGJe_qZWFTMK1c16y6sR65-Kg');
define('ADMIN_ID', '7575052801');

// Web App manzili (HTTPS bo'lishi shart!)
define('WEB_APP_URL', 'https://sizning-saytingiz.com/index.html');

$update = json_decode(file_get_contents('php://input'), true);
$chat_id = $update['message']['chat']['id'] ?? null;
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

$menu = [
    'keyboard' => [
        [['text' => 'BRON QILISH', 'web_app' => ['url' => WEB_APP_URL]]],
        [['text' => 'ADMIN BILAN BOGLANISH']],
        [['text' => 'GAME CLUB JOYLASHUVI']]
    ],
    'resize_keyboard' => true,
    'one_time_keyboard' => false
];

if ($text == '/start') {
    sendMessage($chat_id, "Keldi Botga xush kelibsiz! Quyidagilardan birini tanlang:", $menu);
} elseif ($text == 'ADMIN BILAN BOGLANISH') {
    sendMessage($chat_id, "👤 Admin: Zuxriddinov Boxoviddin\n📞 Telefon: +998886577553\nSavollaringiz bo'lsa, bemalol bog'lanishingiz mumkin.");
} elseif ($text == 'GAME CLUB JOYLASHUVI') {
    $info = "Xush kelibsiz! Bizning Game Club — bu sizning eng yaxshi hordiq maskaningiz!\n\n" .
            "1. Bizda eng so'nggi rusumdagi eng kuchli kompyuterlar va ultra tezkor internet tarmog'i mavjud.\n" .
            "2. Qulay va ergonomik kreslolar, yumshoq muhit sizga haqiqiy geymerlik zavqini taqdim etadi.\n" .
            "3. Do'stlaringiz bilan birga o'yin o'ynash uchun eng ideal va shinam maskan.\n" .
            "4. Sifatli servis va doimo yordamga tayyor operatorlarimiz sizni har doim kutmoqda.\n" .
            "5. Biz har kuni, dam olish kunlarisiz, 24/7 sizning xizmatingizdamiz.\n" .
            "6. Joylashuvimiz juda qulay: Andijon viloyati, Shahrixon tumani markazida.\n" .
            "7. Tojmahal to'yxonasi yonida, barchaga tanish manzilda joylashganmiz.\n" .
            "8. Shunchaki o'yin emas, balki sifatli va maroqli dam olishni tanlang.\n" .
            "9. Biz bilan o'yindan olingan zavq va hissiyotlar yanada yuqori darajada bo'ladi.\n" .
            "10. Tezroq tashrif buyuring, eng zo'r o'yinlar va muhit sizni kutmoqda!";
    sendMessage($chat_id, $info);
}
?>
