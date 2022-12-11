import streamlit as st
import pandas as pd
import numpy as np
import pickle
from io import BytesIO, StringIO

st.title('Final Project AB - Kelompok 9')

# filename = 'finalized_model.sav'
# loaded_model = pickle.load(open(filename, 'rb'))

STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""


class FileUpload(object):

    def __init__(self):
        self.fileTypes = ["png", "jpg"]

    def run(self):
        """
        Upload File on Streamlit Code
        :return:
        """
        st.info(__doc__)
        st.markdown(STYLE, unsafe_allow_html=True)
        file = st.file_uploader("Upload file", type=self.fileTypes)
        show_file = st.empty()
        if not file:
            show_file.info("Please upload a file of type: " +
                           ", ".join(["png", "jpg"]))
            return
        content = file.getvalue()
        if isinstance(file, BytesIO):
            show_file.image(file)
        else:
            data = pd.read_csv(file)
            st.dataframe(data.head(10))
        file.close()


if __name__ == "__main__":
    helper = FileUpload()
    helper.run()
