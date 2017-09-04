import unittest
from unittest.mock import patch
from mycroftapi import MycroftAPI


class MockWS(object):
    def __init__(self):
        pass

    def send(self, message):
        self.message = message


class TestSet(unittest.TestCase):
    @patch('mycroftapi.create_connection')
    def test_mouth_reset(self, mock_create_conn):
        # Create simple replacement websocket object and return it
        # when creating sockets
        mock_ws = MockWS()
        mock_create_conn.return_value = mock_ws
        # Test that init calls create_connection with correct param
        m = MycroftAPI('127.0.0.1')
        mock_create_conn.assert_called_with(
            "ws://" + '127.0.0.1' + ":8181/core")
        # Check that message bus message looks like what we expect
        # Expected data to websocket
        mycroft_type = '"enclosure.mouth.reset"'
        message = '{"type": ' + mycroft_type + '}'
        m.mouth_reset()
        self.assertEqual(message, mock_ws.message)

    @patch('mycroftapi.create_connection')
    def test_mouth_talk(self, mock_create_conn):
        # Create simple replacement websocket object and return it
        # when creating sockets
        mock_ws = MockWS()
        mock_create_conn.return_value = mock_ws
        # Test that init calls create_connection with correct param
        m = MycroftAPI('127.0.0.1')
        mock_create_conn.assert_called_with(
            "ws://" + '127.0.0.1' + ":8181/core")
        # Check that message bus message looks like what we expect
        # Expected data to websocket
        mycroft_type = '"enclosure.mouth.talk"'
        message = '{"type": ' + mycroft_type + '}'
        m.mouth_talk()
        self.assertEqual(message, mock_ws.message)

if __name__ == '__main__':
    unittest.main()
