import socket
import neovim

@neovim.plugin
class Snipper(object):
    def __init__(self, vim):
        # TODO: start the snipper program
        self.vim = vim
        HOST = 'localhost'
        PORT = 53706
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((HOST, PORT))

    @neovim.command('SendLine', sync=True)
    def send_line(self):
        # Set the folloing mapping in the .vimrc TODO: set it in plugin?
        # inoremap <Enter> <C-O>:SendLine<CR><Enter>
        line = self.vim.current.line
        self.socket.sendall(line)
