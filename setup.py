from setuptools import setup, find_packages

setup(
  name = 'stylegan2_pytorch',
  packages = find_packages(),
  scripts=['bin/stylegan2_pytorch'],
  version = '0.19.3',
  license='GPLv3+',
  description = 'StyleGan2 in Pytorch',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/cwvisuals/StyleGAN2',
  download_url = 'https://github.com/cwvisuals/StyleGAN2/blob/test/stylegan2_pytorch-0.20.1.tar.gz',
  keywords = ['generative adversarial networks', 'artificial intelligence'],
  install_requires=[
      'fire',
      'numpy',
      'retry',
      'tqdm',
      'torch',
      'torchvision',
      'pillow',
      'adamp',
      'contrastive_learner>=0.1.0',
      'linear_attention_transformer',
      'vector-quantize-pytorch'
  ],
  classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.6',
  ],
)
