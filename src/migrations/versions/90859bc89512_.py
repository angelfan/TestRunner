"""empty message

Revision ID: 90859bc89512
Revises: 
Create Date: 2018-05-25 15:47:33.368055

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '90859bc89512'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('autotest_Interface',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('module_id', sa.BigInteger(), nullable=True),
    sa.Column('interface_name', sa.String(length=200), nullable=False),
    sa.Column('interface_url', sa.String(length=255), nullable=False),
    sa.Column('interface_header', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('interface_body', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('interface_method', sa.String(length=10), nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), nullable=False),
    sa.Column('datachange_createtime', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('datachange_lasttime', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_autotest_Interface_datachange_lasttime'), 'autotest_Interface', ['datachange_lasttime'], unique=False)
    op.create_index(op.f('ix_autotest_Interface_interface_name'), 'autotest_Interface', ['interface_name'], unique=False)
    op.create_table('autotest_UI_testcase',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('testcase_name', sa.String(length=200), nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), nullable=False),
    sa.Column('datachange_createtime', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('datachange_lasttime', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_autotest_UI_testcase_datachange_lasttime'), 'autotest_UI_testcase', ['datachange_lasttime'], unique=False)
    op.create_table('autotest_interface_testcase',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('interface_url', sa.String(length=255), nullable=False),
    sa.Column('testcase_name', sa.String(length=200), nullable=False),
    sa.Column('module_id', sa.BigInteger(), nullable=False),
    sa.Column('testcase_method', sa.String(length=200), nullable=False),
    sa.Column('testcase_header', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('testcase_body', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('testcase_verification', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), nullable=False),
    sa.Column('datachange_createtime', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('datachange_lasttime', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_autotest_interface_testcase_datachange_lasttime'), 'autotest_interface_testcase', ['datachange_lasttime'], unique=False)
    op.create_table('autotest_module',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('project_id', sa.BigInteger(), nullable=False),
    sa.Column('module_name', sa.String(length=50), nullable=False),
    sa.Column('module_testers', sa.String(length=50), nullable=False),
    sa.Column('module_developer', sa.String(length=50), nullable=False),
    sa.Column('module_version', sa.String(length=100), nullable=False),
    sa.Column('module_desc', sa.String(length=500), nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), nullable=False),
    sa.Column('datachange_createtime', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('datachange_lasttime', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_autotest_module_datachange_lasttime'), 'autotest_module', ['datachange_lasttime'], unique=False)
    op.create_index(op.f('ix_autotest_module_project_id'), 'autotest_module', ['project_id'], unique=False)
    op.create_table('autotest_project',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('project_name', sa.String(length=50), nullable=False),
    sa.Column('project_testers', sa.String(length=50), nullable=False),
    sa.Column('project_developer', sa.String(length=50), nullable=False),
    sa.Column('project_version', sa.String(length=100), nullable=False),
    sa.Column('project_desc', sa.String(length=500), nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), nullable=False),
    sa.Column('datachange_createtime', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('datachange_lasttime', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_autotest_project_datachange_lasttime'), 'autotest_project', ['datachange_lasttime'], unique=False)
    op.create_table('autotest_report',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('testgroup_id', sa.BigInteger(), nullable=False),
    sa.Column('result', sa.BOOLEAN(), nullable=True),
    sa.Column('fail', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('error', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('success', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('total', sa.BigInteger(), nullable=True),
    sa.Column('result_log', sa.Text(), nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), nullable=False),
    sa.Column('datachange_createtime', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('datachange_lasttime', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_autotest_report_datachange_lasttime'), 'autotest_report', ['datachange_lasttime'], unique=False)
    op.create_table('autotest_result',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('report_id', sa.BigInteger(), nullable=False),
    sa.Column('testcase_testgroup_id', sa.BigInteger(), nullable=False),
    sa.Column('result', sa.Integer(), nullable=False),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), nullable=False),
    sa.Column('datachange_createtime', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('datachange_lasttime', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_autotest_result_datachange_lasttime'), 'autotest_result', ['datachange_lasttime'], unique=False)
    op.create_table('autotest_scheduledtask',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('task_name', sa.String(length=50), nullable=False),
    sa.Column('task_type', sa.Integer(), nullable=False),
    sa.Column('module_id', sa.BigInteger(), nullable=False),
    sa.Column('testcase_id', sa.BigInteger(), nullable=False),
    sa.Column('task_desc', sa.String(length=200), nullable=False),
    sa.Column('time_interval', sa.Integer(), nullable=False),
    sa.Column('last_execution_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('next_execution_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('task_result', sa.BOOLEAN(), nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), nullable=False),
    sa.Column('datachange_createtime', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('datachange_lasttime', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_autotest_scheduledtask_datachange_lasttime'), 'autotest_scheduledtask', ['datachange_lasttime'], unique=False)
    op.create_index(op.f('ix_autotest_scheduledtask_module_id'), 'autotest_scheduledtask', ['module_id'], unique=False)
    op.create_index(op.f('ix_autotest_scheduledtask_testcase_id'), 'autotest_scheduledtask', ['testcase_id'], unique=False)
    op.create_table('autotest_testcase_testgroup',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('testcase_group_id', sa.BigInteger(), nullable=False),
    sa.Column('testcase_id', sa.BigInteger(), nullable=False),
    sa.Column('testcase_execution_order', sa.BigInteger(), nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), nullable=True),
    sa.Column('datachange_createtime', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('datachange_lasttime', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_autotest_testcase_testgroup_datachange_lasttime'), 'autotest_testcase_testgroup', ['datachange_lasttime'], unique=False)
    op.create_index(op.f('ix_autotest_testcase_testgroup_testcase_execution_order'), 'autotest_testcase_testgroup', ['testcase_execution_order'], unique=False)
    op.create_index(op.f('ix_autotest_testcase_testgroup_testcase_group_id'), 'autotest_testcase_testgroup', ['testcase_group_id'], unique=False)
    op.create_index(op.f('ix_autotest_testcase_testgroup_testcase_id'), 'autotest_testcase_testgroup', ['testcase_id'], unique=False)
    op.create_table('autotest_testcase_type',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('type_code', sa.BigInteger(), nullable=False),
    sa.Column('type_name', sa.String(length=500), nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_autotest_testcase_type_type_code'), 'autotest_testcase_type', ['type_code'], unique=False)
    op.create_table('autotest_testcasegroup',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('module_id', sa.BigInteger(), nullable=False),
    sa.Column('testcase_group_name', sa.String(length=200), nullable=False),
    sa.Column('testcase_type', sa.BigInteger(), nullable=False),
    sa.Column('testcase_desc', sa.String(length=500), nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), nullable=False),
    sa.Column('datachange_createtime', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('datachange_lasttime', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_autotest_testcasegroup_datachange_lasttime'), 'autotest_testcasegroup', ['datachange_lasttime'], unique=False)
    op.create_index(op.f('ix_autotest_testcasegroup_module_id'), 'autotest_testcasegroup', ['module_id'], unique=False)
    op.create_index(op.f('ix_autotest_testcasegroup_testcase_type'), 'autotest_testcasegroup', ['testcase_type'], unique=False)
    op.create_table('autotest_user',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('login_name', sa.String(length=20), nullable=False),
    sa.Column('user_name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), nullable=False),
    sa.Column('datachange_createtime', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('datachange_lasttime', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_autotest_user_datachange_lasttime'), 'autotest_user', ['datachange_lasttime'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_autotest_user_datachange_lasttime'), table_name='autotest_user')
    op.drop_table('autotest_user')
    op.drop_index(op.f('ix_autotest_testcasegroup_testcase_type'), table_name='autotest_testcasegroup')
    op.drop_index(op.f('ix_autotest_testcasegroup_module_id'), table_name='autotest_testcasegroup')
    op.drop_index(op.f('ix_autotest_testcasegroup_datachange_lasttime'), table_name='autotest_testcasegroup')
    op.drop_table('autotest_testcasegroup')
    op.drop_index(op.f('ix_autotest_testcase_type_type_code'), table_name='autotest_testcase_type')
    op.drop_table('autotest_testcase_type')
    op.drop_index(op.f('ix_autotest_testcase_testgroup_testcase_id'), table_name='autotest_testcase_testgroup')
    op.drop_index(op.f('ix_autotest_testcase_testgroup_testcase_group_id'), table_name='autotest_testcase_testgroup')
    op.drop_index(op.f('ix_autotest_testcase_testgroup_testcase_execution_order'), table_name='autotest_testcase_testgroup')
    op.drop_index(op.f('ix_autotest_testcase_testgroup_datachange_lasttime'), table_name='autotest_testcase_testgroup')
    op.drop_table('autotest_testcase_testgroup')
    op.drop_index(op.f('ix_autotest_scheduledtask_testcase_id'), table_name='autotest_scheduledtask')
    op.drop_index(op.f('ix_autotest_scheduledtask_module_id'), table_name='autotest_scheduledtask')
    op.drop_index(op.f('ix_autotest_scheduledtask_datachange_lasttime'), table_name='autotest_scheduledtask')
    op.drop_table('autotest_scheduledtask')
    op.drop_index(op.f('ix_autotest_result_datachange_lasttime'), table_name='autotest_result')
    op.drop_table('autotest_result')
    op.drop_index(op.f('ix_autotest_report_datachange_lasttime'), table_name='autotest_report')
    op.drop_table('autotest_report')
    op.drop_index(op.f('ix_autotest_project_datachange_lasttime'), table_name='autotest_project')
    op.drop_table('autotest_project')
    op.drop_index(op.f('ix_autotest_module_project_id'), table_name='autotest_module')
    op.drop_index(op.f('ix_autotest_module_datachange_lasttime'), table_name='autotest_module')
    op.drop_table('autotest_module')
    op.drop_index(op.f('ix_autotest_interface_testcase_datachange_lasttime'), table_name='autotest_interface_testcase')
    op.drop_table('autotest_interface_testcase')
    op.drop_index(op.f('ix_autotest_UI_testcase_datachange_lasttime'), table_name='autotest_UI_testcase')
    op.drop_table('autotest_UI_testcase')
    op.drop_index(op.f('ix_autotest_Interface_interface_name'), table_name='autotest_Interface')
    op.drop_index(op.f('ix_autotest_Interface_datachange_lasttime'), table_name='autotest_Interface')
    op.drop_table('autotest_Interface')
    # ### end Alembic commands ###
