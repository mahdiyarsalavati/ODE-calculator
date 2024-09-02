try:
    from StringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

import matplotlib.pyplot as plt


def render_latex(formula, fontsize=12, dpi=300, format_='svg'):
    """Renders LaTeX formula into image."""
    fig = plt.figure()
    text = fig.text(0, 0, u'${0}$'.format(formula), fontsize=fontsize)

    fig.savefig(BytesIO(), dpi=dpi)  # triggers rendering

    bbox = text.get_window_extent()
    width, height = bbox.size / float(dpi) + 0.05
    fig.set_size_inches((width, height))

    dy = (bbox.ymin / float(dpi)) / height
    text.set_position((0, -dy))

    buffer_ = BytesIO()
    fig.savefig(buffer_, dpi=dpi, transparent=True, format=format_)
    plt.close(fig)
    buffer_.seek(0)

    return buffer_

def render_tex_image(tex_string):
    image_bytes = render_latex(tex_string, format_='png')
    with open('formula.png', 'wb') as image_file:
        image_file.write(image_bytes.read())

    