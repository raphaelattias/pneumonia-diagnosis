import torch
from src.models.resnet import get_resnet
from src.models.style_encoder import ConvEncoder


class SuperModel(torch.nn.Module):
    def __init__(self):
        """
        In the constructor we instantiate two nn.Linear modules and assign them as
        member variables.
        """
        super(SuperModel, self).__init__()
        self.image_encoder = get_resnet(50, 2, 0.0625)
        self.image_encoder.load_state_dict(torch.load("models/r50_2x_sk1.pth")['resnet'])
        self.style_encoder =  ConvEncoder()
        self.linear1 = torch.nn.Linear(5376, 512)
        self.linear3 = torch.nn.Linear(512,64)
        self.linear5 = torch.nn.Linear(64,1)
        self.softmax = torch.nn.Sigmoid()
        self.name = "supermodel"

    def forward(self, x):
        """
        In the forward function we accept a Tensor of input data and we must return
        a Tensor of output data. We can use Modules defined in the constructor as
        well as arbitrary operators on Tensors.
        """

        encoded_style = torch.unsqueeze(self.style_encoder(x),0) # Output of style encoder is shape [1024], becomes [1,1280]
        encoded_style = torch.cat((encoded_style,encoded_style,encoded_style,encoded_style,encoded_style),0) # [1,1280] -> [5,1280]

        with torch.no_grad():
            encoded_CXR = self.image_encoder(x) # Output of latent representation is [5, 4096] (each representation of the batch size 5 is 4096)
        self.image_encoder.train()


        X = torch.cat((encoded_CXR,encoded_style),1) # Concatenate [5,4096] with [5,1280] = [5,5376]

        # x_ray = x[:1]
        # style_batch = x[-4:]

        # self.image_encoder.eval()
        # with torch.no_grad():
        #     x_latent = self.image_encoder(x_ray)
        # self.image_encoder.train()

        # style_batch_latent =  torch.unsqueeze(self.style_encoder(style_batch),0)


        y_pred = self.linear1(X)
        y_pred = self.linear3(y_pred)
        y_pred = self.linear5(y_pred)
        y_pred = self.softmax(y_pred)

        return y_pred
