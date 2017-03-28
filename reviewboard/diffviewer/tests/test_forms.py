from reviewboard.diffviewer.diffutils import (get_original_file,
                                              get_patched_file,
                                              patch)

    def test_create(self):
        """Testing UploadDiffForm.create"""
    def test_create_filters_parent_diffs(self):
        """Testing UploadDiffForm.create filters parent diff files"""
    def test_create_with_parser_get_orig_commit_id(self):
        """Testing UploadDiffForm.create uses correct base revision returned
        by DiffParser.get_orig_commit_id
    def test_create_with_parent_filediff_with_move_and_no_change(self):
        """Testing UploadDiffForm.create with a parent diff consisting only
        of a move/rename without content change
        """

        self.spy_on(patch)
        form = UploadDiffForm(
            repository=repository,
            data={
                'basedir': '/',
            },
            files={
                'path': diff,
                'parent_diff_path': parent_diff,
            })
        original_file = get_original_file(f, None, ['ascii'])
        self.assertFalse(patch.spy.called)
        patched_file = get_patched_file(original_file, f, None)
        self.assertTrue(patch.spy.called)
    def test_create_with_parent_filediff_with_move_and_change(self):
        """Testing UploadDiffForm.create with a parent diff consisting of a
        move/rename with content change
        """

        self.spy_on(patch)
        form = UploadDiffForm(
            repository=repository,
            data={
                'basedir': '/',
            },
            files={
                'path': diff,
                'parent_diff_path': parent_diff,
            })
        original_file = get_original_file(f, None, ['ascii'])
        self.assertTrue(patch.spy.called)
        patched_file = get_patched_file(original_file, f, None)
        self.assertEqual(len(patch.spy.calls), 2)