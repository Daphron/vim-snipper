import socket
import neovim
from threading import Thread

@neovim.plugin
class Snipper(object):
    def __init__(self, vim):
        # TODO: start the snipper program
        # TODO: make SURE the snipper program starts
        self.vim = vim
        HOST = 'localhost'
        PORT_IN = 53706
        PORT_OUT = 53707
        self.socket_out = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_out.connect((HOST, PORT_OUT))
        # self.socket_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # # self.socket_in.connect((HOST, PORT_IN))
        # self.socket_in.bind((HOST, PORT_IN))
        # # # self.socket.bind((HOST, PORT))
        # self.socket_in.listen(1)
        # input_thread = Thread(target = self.recieve_snippets)
        # input_thread.start()

        # input_thread.join()
        # self.recieve_snippets()

    @neovim.command('SendLine')
    def send_line(self):
        # Set the folloing mapping in the .vimrc TODO: set it in plugin?
        # inoremap <Enter> <C-O>:SendLine<CR><Enter>
        line = self.vim.current.line
        self.socket_out.sendall(line)   

    def recieve_snippets(self):
        while True:
            # self.conn, self.addr = self.socket_in.accept()
            data = self.conn.recv(1024)
            # if not data:
            #     break
            self.vim.command(":normal i {}".format(data))
        # self.conn.close()

