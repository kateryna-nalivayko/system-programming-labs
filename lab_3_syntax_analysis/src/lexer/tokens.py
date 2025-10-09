TOKEN_SPECS = [
    # --- Коментарі ---
    ("KOMENTAR_BAG",   r"/\*[\s\S]*?\*/"),     # Багаторядковий коментар /* ... */
    ("KOMENTAR_ODN",   r"//[^\n]*"),           # Однорядковий коментар //

    # --- Рядкові та символьні літерали ---
    ("INTERP_STRING",   r'\$"[^"\n]*"'),       # Інтерпольований рядок $"..."
    ("VERBATIM_STRING", r'@".*?"'),            # Вербатим рядок @"..."
    ("LAPKY",           r'"[^"\n]*"'),         # Звичайний рядок
    ("SYM_VOL",         r"'[^']'"),            # Символьний літерал

    # --- Багатосимвольні оператори ---
    ("LAMBDA",        r"=>"),                 # Лямбда-оператор =>
    ("NULL_COALESCE", r"\?\?"),               # ?? оператор об’єднання з null
    ("COND_ACCESS",   r"\?\."),               # ?. умовний доступ
    ("PLUSPLUS",      r"\+\+"),               # Інкремент ++
    ("MINUSMINUS",    r"--"),                 # Декремент --
    ("DVOYNA_KRAPKA2",r"::"),                 # Оператор :: (простір імен)
    ("STRELOCHKA",    r"->"),                 # Вказівник на член структури ->
    ("MENSH_RIVNO",   r"<="),                 # Менше або дорівнює <=
    ("BILSH_RIVNO",   r">="),                 # Більше або дорівнює >=
    ("RIVNO",         r"=="),                 # Порівняння ==
    ("NERIVNO",       r"!="),                 # Нерівність !=

    # --- Односимвольні оператори ---
    ("PRYSVOIENNIA",  r"="),                  # Присвоєння =
    ("MENSH",          r"<"),                 # Менше <
    ("BILSH",          r">"),                 # Більше >
    ("DODAVANNIA",    r"\+"),                 # Додавання +
    ("VIDNIMANNIA",   r"-"),                  # Віднімання -
    ("MNOZHENNIA",    r"\*"),                 # Множення *
    ("DILENNIA",      r"/"),                  # Ділення /
    ("OSTACHA",       r"%"),                  # Остача %
    ("KRAPKA",        r"\."),                 # Крапка .
    ("DVOYNA_KRAPKA", r":"),                  # Двокрапка :

    # --- Розділювачі ---
    ("LAPKA_L",        r"\("),                # Ліва кругла дужка (
    ("LAPKA_R",        r"\)"),                # Права кругла дужка )
    ("DUSHKA_L",       r"\{"),                # Ліва фігурна дужка {
    ("DUSHKA_R",       r"\}"),                # Права фігурна дужка }
    ("KVADRATNA_L",    r"\["),                # Ліва квадратна дужка [
    ("KVADRATNA_R",    r"\]"),                # Права квадратна дужка ]
    ("KOMA",           r","),                 # Кома ,
    ("KRAPKA_Z_COMOYU",r";"),                 # Крапка з комою ;

    # --- Числові літерали ---
    ("CHYSLO_HEX",    r"0[xX][0-9a-fA-F]+"),  # Шістнадцяткове число
    ("CHYSLO",        r"\d+(\.\d+)?"),        # Ціле або десяткове число

    # --- Ключові слова ---
    ("IF",      r"\bif\b"),                   # if
    ("ELSE",    r"\belse\b"),                 # else
    ("WHILE",   r"\bwhile\b"),                # while
    ("FOR",     r"\bfor\b"),                  # for
    ("RETURN",  r"\breturn\b"),               # return
    ("CLASS",   r"\bclass\b"),                # class
    ("VOID",    r"\bvoid\b"),                 # void
    ("INT",     r"\bint\b"),                  # int
    ("FLOAT",   r"\bfloat\b"),                # float
    ("DOUBLE",  r"\bdouble\b"),               # double
    ("BOOL",    r"\bbool\b"),                 # bool
    ("STRING",  r"\bstring\b"),               # string
    ("TRUE",    r"\btrue\b"),                 # true
    ("FALSE",   r"\bfalse\b"),                # false
    ("NULL",    r"\bnull\b"),                 # null

    # --- Ідентифікатори ---
    ("ZMINNA",  r"[a-zA-Z_][a-zA-Z0-9_]*"),   # Ідентифікатор (змінна, функція)
