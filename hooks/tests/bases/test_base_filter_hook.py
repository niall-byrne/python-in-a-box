"""Test the BaseHookFilter class."""

from unittest import TestCase
from unittest.mock import Mock, call, patch

from ...post_gen_project import BaseHook, BaseHookFilter
from ..fixtures.concrete_filter_hook import ConcreteBaseHookFilter


class TestBaseHook(TestCase):
    """Test the BaseHookFilter class."""

    def setUp(self) -> None:
        self.instance = ConcreteBaseHookFilter()

    def test_initialize__has_correct_properties(self) -> None:
        self.assertIsInstance(self.instance, BaseHook)
        self.assertIsInstance(self.instance, BaseHookFilter)

    @patch("os.path.exists")
    @patch("os.remove")
    @patch("shutil.rmtree")
    def test_remove__when_files_do_not_exist__no_exception(
        self,
        m_rmtree: Mock,
        m_remove: Mock,
        m_exists: Mock,
    ) -> None:
        m_exists.side_effect = [False, False, False]

        self.instance.hook()

        m_exists.assert_has_calls(list(map(call, self.instance.excluded)))
        m_remove.assert_not_called()
        m_rmtree.assert_not_called()

    @patch("os.path")
    @patch("os.remove")
    @patch("shutil.rmtree")
    def test_remove__when_files_exist__removes_files(
        self,
        m_rmtree: Mock,
        m_remove: Mock,
        m_path: Mock,
    ) -> None:
        m_path.exists.side_effect = [True, True, True]
        m_path.isfile.side_effect = [False, True, False]
        m_path.isdir.side_effect = [False, False, True]

        self.instance.hook()

        m_path.exists.assert_has_calls(list(map(call, self.instance.excluded)))
        m_remove.assert_called_once_with(self.instance.excluded[1])
        m_rmtree.assert_called_once_with(self.instance.excluded[2])
