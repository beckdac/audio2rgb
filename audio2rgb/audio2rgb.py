import os
import tempfile
import datetime

from pydub import AudioSegment


class Audio2RGB(object):
    '''
    Convert an input audio file into a series of time synced
    RGB triplets.
    '''

    def __init__(self, inputFilename, verbose, debug):
        self.inputFilename = inputFilename;
        self.verbose = verbose;
        self.debug = debug;
        self.tmpFile = tempfile.NamedTemporaryFile(delete=False)

        if self.debug:
            print('temporary file is {0}'.format(self.tmpFile.name))

        if self.verbose:
            print('preprocessing audio from {0}'.format(inputFilename))
        startTime = datetime.datetime.now()

        # autodetect and decompress into memory
        self.audioSample = AudioSegment.from_file(inputFilename)
        # down sample from stereo to mono
        self.audioSample = self.audioSample.set_channels(1)

        endTime = datetime.datetime.now()
        if self.verbose:
            dT = endTime - startTime
            print('preprocessing took {:.2f} seconds'.format(
                dT.total_seconds()
                ))

    def __del__(self):
        if self.debug:
            print('Augio2RGB destructor called')
        # cleanup the temporary file
        self.tmpFile.close()
        if not self.debug:
            os.unlink(self.tmpFile.name)
        #else:
        #    print('temporary file {0} not deleted'.format(
        #        self.tmpFile.name
        #        ))
