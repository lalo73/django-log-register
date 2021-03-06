"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from log_register.models import Lot
from log_register.settings import INFO, SUCCESS


class LogRegisterTest(TestCase):
    def setUp(self):
        self.lot_default = Lot()
        self.lot_default.save()

    def test_when_create_a_lot_then_the_register_start_is_set(self):
        self.assertIsNotNone(self.lot_default.register_start)

    def test_when_create_a_lot_then_the_register_end_is_None(self):
        self.assertIsNone(self.lot_default.register_end)

    def test_by_default_a_lot_is_not_single(self):
        self.assertFalse(self.lot_default.single)

    def test_by_default_a_lot_have_not_a_generic_reference(self):
        self.assertIsNone(self.lot_default.object_id)
        self.assertIsNone(self.lot_default.content_type)

    def test_when_create_a_lot_the_count_of_info_logs_is_zero(self):
        self.assertEqual(self.lot_default.info_count(), 0)

    def test_when_create_a_lot_the_count_of_error_logs_is_zero(self):
        self.assertEqual(self.lot_default.error_count(), 0)

    def test_when_create_a_lot_the_count_of_warning_logs_is_zero(self):
        self.assertEqual(self.lot_default.warning_count(), 0)

    def test_when_create_a_lot_the_count_of_debug_logs_is_zero(self):
        self.assertEqual(self.lot_default.debug_count(), 0)

    def test_when_create_a_lot_the_count_of_success_logs_is_zero(self):
        self.assertEqual(self.lot_default.success_count(), 0)

    def test_when_create_a_lot_there_is_no_logs(self):
        self.assertFalse(self.lot_default.logs.all())

    def test_when_call_close_method_then_the_register_end_is_set(self):
        self.lot_default.close()
        self.assertIsNotNone(self.lot_default.register_end)

    def test_when_call_success_method_then_a_log_with_level_success_is_created(self):
        self.assertEqual(self.lot_default.success_count(), 0)
        success_logs = self.lot_default.logs.filter(level=SUCCESS)
        self.assertEqual(len(success_logs), 0)
        self.lot_default.success("testing", "extra_data_test")
        self.assertEqual(self.lot_default.success_count(), 1)
        success_logs = self.lot_default.logs.filter(level=SUCCESS)
        self.assertEqual(len(success_logs), 1)

    def test_when_call_info_method_then_a_log_with_level_info_is_created(self):
        self.assertEqual(self.lot_default.info_count(), 0)
        info_logs = self.lot_default.logs.filter(level=INFO)
        self.assertEqual(len(info_logs), 0)
        self.lot_default.info("testing", "extra_data_test")
        self.assertEqual(self.lot_default.info_count(), 1)
        info_logs = self.lot_default.logs.filter(level=INFO)
        self.assertEqual(len(info_logs), 1)