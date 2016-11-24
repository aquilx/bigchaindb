from bigchaindb.util import verify_vote_signature
from bigchaindb.common.schema import validate_vote_schema, SchemaValidationError


class BaseConsensusRules():
    """Base consensus rules for Bigchain.
    """

    @staticmethod
    def validate_transaction(bigchain, transaction):
        """See :meth:`bigchaindb.models.Transaction.validate`
        for documentation.

        """
        return transaction.validate(bigchain)

    @staticmethod
    def validate_block(bigchain, block):
        """See :meth:`bigchaindb.models.Block.validate` for documentation."""
        return block.validate(bigchain)

    @staticmethod
    def verify_vote(voters, signed_vote):
        """Verify the signature of a vote.

        Refer to the documentation of
        :func:`bigchaindb.util.verify_signature`.
        """
        try:
            validate_vote_schema(signed_vote)
        except SchemaValidationError:
            # TODO: log this.
            return False
        else:
            return verify_vote_signature(voters, signed_vote)
