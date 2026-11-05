package example;

/* metamodel_version: 1.12.0 */
/* version: 1.6.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  One edition of the D3FEND ontology, with its header and all its entries.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class D3fendCatalog  {

  private List<String> comment;
  private String releaseDate;
  private URI ontologyIri;
  private String versionInfo;
  private URI versionIri;
  private String ontologyTitle;
  private String ontologyDescription;
  private String ontologyLicense;
  private List<D3fendDisjointGroup> disjointGroups;
  private List<D3fendEntry> entries;


}