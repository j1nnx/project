def mask_card_or_account(input_str):
    """принимает на вход строку информацией тип карты/счета и номер карты/счета"""
    def mask_card(card_num):
        """возвращает эту строку с замаскированным номером карты"""
        if len(card_num) < 16:
            return card_num
        return card_num[:8] + ' ** **' + card_num[-4:]

    def mask_account(account_num):
        """возвращает эту строку с замаскированным номером счета."""
        return '**' + account_num[-4:]

    words = input_str.split()
    if words[0].lower() in ['visa', 'mastercard', 'maestro']:
        return words[0] + ' ' + ' '.join(words[1:-1]) + ' ' + mask_card(words[-1])
    elif words[0].lower() == 'счет':
        return 'Счет ' + mask_account(words[1])

