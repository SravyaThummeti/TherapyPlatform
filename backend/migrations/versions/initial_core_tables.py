"""
Initial core tables for Therapist Platform

Revision ID: initial_core_tables
Revises: 6561b105adda
Create Date: 2025-07-24 00:00:00.000000
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'initial_core_tables'
down_revision = '6561b105adda'
branch_labels = None
depends_on = None


def upgrade():
    # --- 1) Base tables ---
    op.create_table(
        'patients',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('first_name', sa.String(length=50), nullable=False),
        sa.Column('last_name', sa.String(length=50), nullable=False),
        sa.Column('dob', sa.Date(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )
    op.create_table(
        'therapists',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('first_name', sa.String(length=50), nullable=False),
        sa.Column('last_name', sa.String(length=50), nullable=False),
        sa.Column('npi', sa.String(length=20), nullable=False, unique=True),
        sa.Column('clinic_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )
    op.create_index('ix_therapists_clinic_id', 'therapists', ['clinic_id'])

    op.create_table(
        'referring_providers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('phone', sa.String(length=20)),
        sa.Column('email', sa.String(length=120)),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )

    op.create_table(
        'insurances',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('payer_id', sa.String(length=50), unique=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )

    op.create_table(
        'clinics',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('address', sa.String(length=200), nullable=False),
        sa.Column('fax', sa.String(length=20)),
        sa.Column('npi', sa.String(length=20), unique=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )

    # --- 2) Referral Requests ---
    op.create_table(
        'referral_requests',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('patient_id', sa.Integer(), sa.ForeignKey('patients.id'), nullable=False),
        sa.Column('discipline', sa.String(length=50), nullable=False),
        sa.Column('notes', sa.Text(), nullable=False),
        sa.Column('referring_provider_id', sa.Integer(), sa.ForeignKey('referring_providers.id'), nullable=False),
        sa.Column('physician_name', sa.String(length=100), nullable=False),
        sa.Column('physician_signature', sa.String(length=200)),
        sa.Column('physician_signed_at', sa.Date()),
        sa.Column('requested_at', sa.Date(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )
    op.create_index('ix_ref_req_patient', 'referral_requests', ['patient_id'])

    # --- 3) Authorizations ---
    op.create_table(
        'authorizations',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('patient_id', sa.Integer(), sa.ForeignKey('patients.id'), nullable=False),
        sa.Column('therapist_id', sa.Integer(), sa.ForeignKey('therapists.id'), nullable=False),
        sa.Column('insurance_id', sa.Integer(), sa.ForeignKey('insurances.id'), nullable=False),
        sa.Column('referral_id', sa.Integer(), sa.ForeignKey('referral_requests.id'), nullable=True),
        sa.Column('start_date', sa.Date(), nullable=False),
        sa.Column('end_date', sa.Date(), nullable=False),
        sa.Column('visits_authorized', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )
    op.create_index('ix_auth_therapist', 'authorizations', ['therapist_id'])