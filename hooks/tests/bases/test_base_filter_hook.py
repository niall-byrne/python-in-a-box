"""Test the BaseHookFilter class."""

from unittest.mock import Mock, call, patch

from hooks.post_gen_project import BaseHook, BaseHookFilter


class TestBaseHook:
    """Test the BaseHookFilter class."""

    def test_instance__when_initialized__has_correct_inheritance(
        self,
        concrete_base_filter_hook: BaseHookFilter,
    ) -> None:
        assert isinstance(concrete_base_filter_hook, BaseHook)
        assert isinstance(concrete_base_filter_hook, BaseHookFilter)

    @patch("os.path.exists")
    @patch("os.remove")
    @patch("shutil.rmtree")
    def test_remove__when_files_do_not_exist__no_exception(
        self,
        m_rmtree: Mock,
        m_remove: Mock,
        m_exists: Mock,
        concrete_base_filter_hook: BaseHookFilter,
    ) -> None:
        m_exists.side_effect = [False, False, False]

        concrete_base_filter_hook.hook()

        m_exists.assert_has_calls(
            list(map(call, concrete_base_filter_hook.excluded))
        )
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
        concrete_base_filter_hook: BaseHookFilter,
    ) -> None:
        m_path.exists.side_effect = [True, True, True]
        m_path.isfile.side_effect = [False, True, False]
        m_path.isdir.side_effect = [False, False, True]

        concrete_base_filter_hook.hook()

        m_path.exists.assert_has_calls(
            list(map(call, concrete_base_filter_hook.excluded))
        )
        m_remove.assert_called_once_with(concrete_base_filter_hook.excluded[1])
        m_rmtree.assert_called_once_with(concrete_base_filter_hook.excluded[2])
