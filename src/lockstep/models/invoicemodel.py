#
# Lockstep Software Development Kit for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Ted Spence <tspence@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass
from lockstep.models.invoiceaddressmodel import InvoiceAddressModel
from lockstep.models.invoicelinemodel import InvoiceLineModel
from lockstep.models.invoicepaymentdetailmodel import InvoicePaymentDetailModel
from lockstep.models.notemodel import NoteModel
from lockstep.models.attachmentmodel import AttachmentModel
from lockstep.models.companymodel import CompanyModel
from lockstep.models.companymodel import CompanyModel
from lockstep.models.contactmodel import ContactModel
from lockstep.models.creditmemoinvoicemodel import CreditMemoInvoiceModel
from lockstep.models.customfieldvaluemodel import CustomFieldValueModel
from lockstep.models.customfielddefinitionmodel import CustomFieldDefinitionModel

@dataclass
class InvoiceModel:
    """
    An Invoice represents a bill sent from one company to another. The
    creator of the invoice is identified by the `CompanyId` field, and
    the recipient of the invoice is identified by the `CustomerId`
    field. Most invoices are uniquely identified both by a Lockstep
    Platform ID number and a customer ERP "key" that was generated by
    the system that originated the invoice. Invoices have a total amount
    and a due date, and when some payments have been made on the Invoice
    the `TotalAmount` and the `OutstandingBalanceAmount` may be
    different.
    """

    groupKey: str = None
    invoiceId: str = None
    companyId: str = None
    customerId: str = None
    erpKey: str = None
    purchaseOrderCode: str = None
    referenceCode: str = None
    salespersonCode: str = None
    salespersonName: str = None
    invoiceTypeCode: str = None
    invoiceStatusCode: str = None
    termsCode: str = None
    specialTerms: str = None
    currencyCode: str = None
    totalAmount: float = None
    salesTaxAmount: float = None
    discountAmount: float = None
    outstandingBalanceAmount: float = None
    invoiceDate: str = None
    discountDate: str = None
    postedDate: str = None
    invoiceClosedDate: str = None
    paymentDueDate: str = None
    importedDate: str = None
    primaryOriginAddressId: str = None
    primaryBillToAddressId: str = None
    primaryShipToAddressId: str = None
    created: str = None
    createdUserId: str = None
    modified: str = None
    modifiedUserId: str = None
    appEnrollmentId: str = None
    isVoided: bool = None
    inDispute: bool = None
    excludeFromAging: bool = None
    addresses: list[InvoiceAddressModel] = None
    lines: list[InvoiceLineModel] = None
    payments: list[InvoicePaymentDetailModel] = None
    notes: list[NoteModel] = None
    attachments: list[AttachmentModel] = None
    company: CompanyModel = None
    customer: CompanyModel = None
    customerPrimaryContact: ContactModel = None
    creditMemos: list[CreditMemoInvoiceModel] = None
    customFieldValues: list[CustomFieldValueModel] = None
    customFieldDefinitions: list[CustomFieldDefinitionModel] = None

