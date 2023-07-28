import timm
from DeepImageSearch import Load_Data, Search_Setup
from unittest import mock

def getSimilarImages(path):
    timm.list_models(pretrained=True)
    
    # Patch the input function to return "no" automatically
    with mock.patch('builtins.input', return_value='no'):
        # Pre-extract metadata and features
        dl = Load_Data()
        img_list = dl.from_folder(['C:\\Users\\hp\\Desktop\\ecom - Copy\\project\\store\\Img_Search\\Images'])
        
        # Use the pre-extracted data in Search_Setup
        st = Search_Setup(img_list, model_name="vgg19", pretrained=True, image_count=None)
        st.run_index()

        similar_images = st.get_similar_images(path, number_of_images=6)
        similar_images = {int(k): v for k, v in similar_images.items()}
        # Update metadata
        metadata = st.get_image_metadata_file()

    return similar_images














