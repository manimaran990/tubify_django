"""
Backs up and restores a settings file to Dropbox.
This is an example app for API v2.
"""

import sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
import configparser as cfg


class Drop_to_Box(object):
    def __init__(self, config):
        # self.token = self.read_token_from_config(config)
        self.token = 'm2bePg_r7I0AAAAAAAAAASB4MncYH9EVGHIBkfqFzvjAeGL00UZ_BPGugqz2PQ8s'

    def read_token_from_config(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', "token")

    # Uploads contents of LOCALFILE to Dropbox

    def upload_dbx(self, dbx, localfile, backup_path):
        with open(localfile, 'rb') as f:
            # We use WriteMode=overwrite to make sure that the settings in the file
            # are changed on upload
            print("Uploading " + localfile +
                  " to Dropbox as " + backup_path + "...")
            try:
                dbx.files_upload(f.read(), backup_path,
                                 mode=WriteMode('overwrite'))
            except ApiError as err:
                # This checks for the specific error where a user doesn't have
                # enough Dropbox space quota to upload this file
                if (err.error.is_path() and
                        err.error.get_path().reason.is_insufficient_space()):
                    sys.exit("ERROR: Cannot back up; insufficient space.")
                elif err.user_message_text:
                    print(err.user_message_text)
                    sys.exit()
                else:
                    print(err)
                    sys.exit()

    
    # # Change the text string in LOCALFILE to be new_content
    # # @param new_content is a string
    # def change_local_file(self, new_content):
    #     print("Changing contents of " + LOCALFILE + " on local machine...")
    #     with open(LOCALFILE, 'wb') as f:
    #         f.write(new_content)

    # # Restore the local and Dropbox files to a certain revision
    # def restore(self, rev=None):
    #     # Restore the file on Dropbox to a certain revision
    #     print("Restoring " + BACKUPPATH +
    #           " to revision " + rev + " on Dropbox...")
    #     dbx.files_restore(BACKUPPATH, rev)

    #     # Download the specific revision of the file at BACKUPPATH to LOCALFILE
    #     print("Downloading current " + BACKUPPATH +
    #           " from Dropbox, overwriting " + LOCALFILE + "...")
    #     dbx.files_download_to_file(LOCALFILE, BACKUPPATH, rev)

    # # Look at all of the available revisions on Dropbox, and return the oldest one
    # def select_revision():
    #     # Get the revisions for a file (and sort by the datetime object, "server_modified")
    #     print("Finding available revisions on Dropbox...")
    #     entries = dbx.files_list_revisions(BACKUPPATH, limit=30).entries
    #     revisions = sorted(entries, key=lambda entry: entry.server_modified)

    #     for revision in revisions:
    #         print(revision.rev, revision.server_modified)

    #     # Return the oldest revision (first entry, because revisions was sorted oldest:newest)
    #     return revisions[0].rev

    ''' 
        check for auth token and try to get current account
    '''

    def send_to_dbx(self, localfile, backup_path):
        if (len(self.token) == 0):
            sys.exit("ERROR: Looks like you didn't add your access token. "
                     "Open up backup-and-restore-example.py in a text editor and "
                     "paste in your token in line 14.")

        # Create an instance of a Dropbox class, which can make requests to the API.
        print("Creating a Dropbox object...")
        with dropbox.Dropbox(self.token) as dbx:

            # Check that the access token is valid
            try:
                dbx.users_get_current_account()

            except AuthError:
                sys.exit("ERROR: Invalid access token; try re-generating an "
                         "access token from the app console on the web.")

            self.upload_dbx(dbx, localfile, backup_path)

        # # Create a backup of the current settings file
        # backup()

        # # Change the user's file, create another backup
        # change_local_file(b"updated")
        # backup()

        # # Restore the local and Dropbox files to a certain revision
        # to_rev = select_revision()
        # restore(to_rev)

        # print("Done!")
