class LeftPadUtils:
    SPACE = " "

    @staticmethod
    def is_empty(cs):
        return cs is None or len(cs) == 0

    @staticmethod
    def left_pad(str_, size, pad_str):
        """Left pad a String with a specified String.

        Pad to a size of the given size.

        :param str_: the String to pad out, may be None
        :param size: the size to pad to
        :param pad_str: the String to pad with, None or empty treated as single space
        :return: left padded String or original String if no padding is necessary,
            None if None String input
        """
        if str_ is None:
            return None

        if LeftPadUtils.is_empty(pad_str):
            pad_str = LeftPadUtils.SPACE

        pad_len = len(pad_str)
        str_len = len(str_)
        pads = size - str_len
        if pads <= 0:
            return str_
        if pads == pad_len:
            return pad_str + str_
        elif pads < pad_len:
            return pad_str[:pads] + str_
        else:
            padding = [pad_str[i % pad_len] for i in range(pads)]
            return "".join(padding) + str_
