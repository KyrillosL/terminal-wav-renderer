from scipy.signal import resample
from sklearn.preprocessing import minmax_scale
VERTICAL_BAR_CHARS = [u'\u2581', u'\u2582', u'\u2583', u'\u2584', u'\u2585', u'\u2586', u'\u2587', u'\u2588']


# Input an audio buffer, render a representation in the terminal
# Using the PEP-8 79 max line length characters
def render_wav(audio):
    max_len_chars = len(VERTICAL_BAR_CHARS) - 1
    resampled = resample(audio, 79)
    normalized = minmax_scale(resampled, feature_range=(0, 1), axis=0, copy=True)
    for n in normalized:
        print(VERTICAL_BAR_CHARS[int(n * max_len_chars)], end='')
    print()
